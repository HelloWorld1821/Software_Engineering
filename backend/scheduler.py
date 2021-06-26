from const import DEFAULT_TMP, FEE_PER_KWH, KWH_PER_MIN, POWER_OFF_TMP_PER_MIN, TMP_PER_MIN
from database import *
import threading
from time import sleep
from queuee import Queuee
from service_object import ServiceObject
from rooom import Rooom

class Scheduler:
    def __init__(self) -> None:
        self.mode = 'cold'
        self.fee_rate = 1.0
        self.temp_section = [18,26,26,30]
        self.default_temp = 26
        self.schedule_num = 3
        self.SLAVE_NUM = 4
        self.RR_SLOT = 60   #时间片调度间隔：60s

        self.queue = Queuee()
        self.max_object_num = 3

        self.rooms = {}
        for i in range(self.SLAVE_NUM):
            self.rooms[100+i+1] = Rooom(room_id=100+i+1,current_temp=self.default_temp)

        # 调度队列
        self.blowing_list = []
        self.schedule_queue = []

    # 更新服务时间、等待时间、费用、当前温度
    def update(self):

        mode_factor = -1 if self.mode == 'cold' else 1

        # 更新等待时间
        with self.queue.wait_lock:
            for item in self.queue.wait_queue:
                item[-1].wait_clock += 1
        # 更新循环时间
        with self.queue.service_lock:
            for room_id in self.queue.service_queue:
                self.queue.service_queue[room_id].service_clock += 1
        # 更新费用和当前温度
        for room_id in self.rooms:
            # print('room_id = ',room_id)
            if room_id in self.queue.service_queue:
                self.rooms[room_id].current_temp += TMP_PER_MIN[self.queue.service_queue[room_id].current_speed] / 60 * mode_factor
                self.rooms[room_id].fee += KWH_PER_MIN[self.queue.service_queue[room_id].current_speed] / 60 * self.fee_rate
                Room.query.filter(Room.room_id == room_id).update({
                    "mode":self.mode,
                    "speed":self.queue.service_queue[room_id].current_speed,
                    "current_temp":self.rooms[room_id].current_temp,
                    "target_temp":self.rooms[room_id].target_temp,
                    "state":"SENDING"
                })  
            elif self.rooms[room_id].current_temp * mode_factor > self.default_temp* mode_factor:
                self.rooms[room_id].current_temp -= POWER_OFF_TMP_PER_MIN /60 * mode_factor
                Room.query.filter(Room.room_id == room_id).update({
                    "mode":self.mode,
                    "speed":"ZERO",
                    "current_temp":self.rooms[room_id].current_temp,
                    "target_temp":self.rooms[room_id].target_temp,
                    "state":"NOTSENDING"
                })
            db.session.commit()
        
    
    # 调度
    def schedule(self):  
        while True:
            sleep(1)
            self.update()
            
            object = self.queue.get_from_wait_queue()
            if object is None:
                # 等待队列为空
                continue
            elif len(self.queue.service_queue)< self.max_object_num:
                # 等待队列不为空 且 服务队列仍然有空位
                self.queue.pop_wait_queue()
                self.queue.add_into_service_queue(object)
                self.rooms[object.room_id].power_on()
                self.rooms[object.room_id].current_speed=self.rooms[object.room_id].target_speed
            else:
                # 服务队列已满
                object_with_lowest_priority = self.queue.get_service_object_with_lowest_priority_from_service_queue()

                if object.priority < object_with_lowest_priority.priority:
                    # 优先级调度
                    print('优先级调度')
                    self.queue.pop_wait_queue()
                    self.queue.add_into_service_queue(object)
                    self.rooms[object.room_id].power_on()
                    self.rooms[object.room_id].current_speed=self.rooms[object.room_id].target_speed
                    if len(self.queue.service_queue) != self.max_object_num:
                        self.queue.pop_service_by_room_id(object_with_lowest_priority.room_id)
                        self.queue.add_into_wait_queue(object_with_lowest_priority)
                        self.rooms[object_with_lowest_priority.room_id].power_off()
                        self.rooms[object_with_lowest_priority.room_id].current_speed = None
                elif object.priority == object_with_lowest_priority.priority:
                    # 时间片轮转
                    if object.wait_clock >= self.RR_SLOT:  # 等待时间已满，强行替换
                        print('时间片调度')
                        self.queue.pop_wait_queue()
                        self.queue.add_into_service_queue(object)
                        self.rooms[object.room_id].power_on()
                        self.rooms[object.room_id].current_speed=self.rooms[object.room_id].target_speed
                        if len(self.queue.service_queue) != self.max_object_num:
                            self.queue.pop_service_by_room_id(object_with_lowest_priority.room_id)
                            self.queue.add_into_wait_queue(object_with_lowest_priority)
                            self.rooms[object_with_lowest_priority.room_id].power_off()
                            self.rooms[object_with_lowest_priority.room_id].current_speed = None

    # 设置参数
    def set_para(self,mode,fee_rate,temp_section,default_temp,schedule_num):
        self.mode = mode
        self.fee_rate = fee_rate
        self.temp_section = temp_section
        self.default_temp = default_temp
        self.schedule_num = schedule_num
    
    # 获取房间状态
    def get_slave_state(self,roomId):
        print('roomid = ',roomId)
        if 100 < roomId and roomId < 100 + self.SLAVE_NUM+1:
            return self.rooms[roomId].get_state()
        return {}
    
    # 处理开机、关机、调温、调风请求
    def deal_with_require(self, roomId, targetTemp,targetSpeed,acState):
        if acState == 'On':
            # 送风
            # if self.rooms[roomId].power == False:
            #     self.rooms[roomId].power_on()
            if targetSpeed == self.rooms[roomId].get_target_speed():
                # 说明是调温指令
                self.rooms[roomId].set_target_temp(targetTemp)
                print('调温')
                self.make_service_object(self.rooms[roomId])
            else:
                # 说明是调风指令
                self.rooms[roomId].set_target_speed(targetSpeed)
                self.rooms[roomId].set_target_temp(targetTemp)
                print('调风')
                self.make_service_object(self.rooms[roomId])
        else:
            # 不送风
            self.rooms[roomId].power_off()
            # with self.queue.service_lock:
            print('111111111111111111111111111111111111')
            if roomId in self.queue.service_queue:
                print('222222222222222222222222222222222222')
                self.queue.pop_service_by_room_id(roomId)
                print('3333333333333333333333333333333333333333333333333')
                self.rooms[roomId].power_off()
                self.rooms[roomId].current_speed = None
                # del self.queue.service_queue[roomId]
            # with self.queue.wait_lock:
            print('44444444444444444444444444444444444444444')
            for index, wait_obi in enumerate(self.queue.wait_queue):
                print('55555555555555555555555555555555555555555')
                if wait_obi[-1].room_id == roomId:
                    print('6666666666666666666666666666666666666666666666')
                    del self.queue.wait_queue[index]
            print('不送风')

    # 创建服务对象,并加入等待队列
    def make_service_object(self,rooom:Rooom):
        object = self.queue.create_service_object(rooom.room_id,rooom.current_temp,rooom.current_speed,rooom.target_temp,rooom.target_speed)
        self.queue.add_into_wait_queue(object)
