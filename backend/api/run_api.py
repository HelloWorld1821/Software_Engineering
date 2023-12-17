#调度部分
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from sql import db_models
from sql.db_models import get_db
from datetime import datetime
import threading

router = APIRouter(prefix="/schedule", tags=["schedule"])

#服务队列
serving_rooms=[]
#等待队列
pending_rooms=[]
#所有房间
all_rooms=[]

#优先级调度
def priority(db):

    global serving_rooms,pending_rooms,all_rooms

    #字典映射，将风速的字符串映射为相应的整数值
    speed_mapping = {'high': 3, 'medium': 2, 'low': 1}

    all_rooms.sort(key=lambda x: speed_mapping[x.fan_speed], reverse=True)
    serving_rooms.sort(key=lambda x: speed_mapping[x.fan_speed])

    #如果服务队列不满，且等待队列不为空，则将等待队列中的房间加入服务队列
    if(len(serving_rooms)<3 and len(pending_rooms)!=0):
        for room in pending_rooms.copy():
            if(len(serving_rooms)<3):
                for temp in pending_rooms :
                    if temp==room:
                        pending_rooms.remove(temp)
                        serving_rooms.append(temp)
                        temp.status='SERVING'
                        db_room = db.query(db_models.Room).filter(db_models.Room.room_id == temp.room_id).first()
                        db_room.status='SERVING'
                        db.commit()
                        break
            else:
                break

    #如果服务队列满了，且等待队列不为空，则将服务队列中的房间与等待队列中的房间进行优先级比较，优先级高的房间加入服务队列，优先级低的房间加入等待队列
    for room in pending_rooms.copy():
        for service in serving_rooms.copy():
            if(room.status=='WAITING'and speed_mapping[room.fan_speed] > speed_mapping[service.fan_speed]):
                for temp in serving_rooms:
                    if temp==service:
                        serving_rooms.remove(temp)
                        pending_rooms.append(temp)
                        temp.status='WAITING'
                        db_room = db.query(db_models.Room).filter(db_models.Room.room_id == temp.room_id).first()
                        db_room.status='WAITING'
                        db.commit()
                        break
                
                for temp in pending_rooms:
                    if temp==room:
                        pending_rooms.remove(temp)
                        serving_rooms.append(temp)
                        temp.status='SERVING'
                        db_room = db.query(db_models.Room).filter(db_models.Room.room_id == temp.room_id).first()
                        db_room.status='SERVING'
                        db.commit()
                        break
                break

#时间片轮询
def time_slice(db):
    speed_mapping = {'high': 3, 'medium': 2, 'low': 1}

    global serving_rooms,pending_rooms,all_rooms

    #如果服务队列中有房间，且等待队列不为空，则将服务队列中的房间与等待队列中的房间进行优先级比较，优先级高的房间加入服务队列，优先级低的房间加入等待队列
    if(len(serving_rooms)==3 and len(pending_rooms)!=0):
        for room in serving_rooms.copy():
            for pend in pending_rooms.copy():
                if room.server_time>=20 and speed_mapping[room.fan_speed] == speed_mapping[pend.fan_speed]:
                    for temp in serving_rooms:
                        if temp==room:
                            serving_rooms.remove(temp)
                            pending_rooms.append(temp)
                            temp.status='WAITING'
                            db_room = db.query(db_models.Room).filter(db_models.Room.room_id == temp.room_id).first()
                            db_room.status='WAITING'
                            db.commit()
                            break

                    for temp in pending_rooms:
                        if temp==pend:
                            pending_rooms.remove(temp)
                            serving_rooms.append(temp)
                            temp.status='SERVING'
                            db_room = db.query(db_models.Room).filter(db_models.Room.room_id == temp.room_id).first()
                            db_room.status='SERVING'
                            db.commit()
                            break
                    break

def schedule(db):

    global serving_rooms,pending_rooms,all_rooms
    temp_queue=serving_rooms.copy()

    priority(db)
    time_slice(db)
    priority(db)

    #遍历服务队列，如果服务时间超过20秒，则将其加入等待队列
    for room in temp_queue:
        if room.status=='WAITING':
            for temp in all_rooms:
                if temp==room:
                    #结束一个详单
                    db_record = db.query(db_models.Record).filter(db_models.Record.record_id == temp.record_id).first()
                    db_record.end_time=datetime.now()
                    db_record.duration=temp.server_time
                    db_record.current_cost=temp.total_cost-db_record.current_cost
                    db.commit()
                    # 新建一个详单
                    db_record = db_models.Record(room_id=temp.room_id, request_time=datetime.now(), fan_speed=temp.fan_speed,current_cost=temp.total_cost)
                    db_room = db.query(db_models.Room).filter(db_models.Room.room_id == temp.room_id).first()
                    db_room.server_time=0
                    temp.server_time=0
                    db.add(db_record)
                    db.commit()
                    db_room.record_id=db_record.record_id
                    temp.record_id=db_record.record_id
                    db.commit()
                    break
    
    #遍历服务队列，服务时间加10秒
    for service in serving_rooms:
        service.server_time+=10
        db_room = db.query(db_models.Room).filter(db_models.Room.room_id == service.room_id).first()
        db_room.server_time+=10
        db.commit()
        if service not in temp_queue:
            # 更新一个详单
            db_record = db.query(db_models.Record).filter(db_models.Record.record_id == service.record_id).first()
            db_record.start_time=datetime.now()
            db.commit()

# 遍历所有房间，计算费用
def calculate_cost(db):
    global serving_rooms,pending_rooms,all_rooms
    for room in all_rooms:
        db_room = db.query(db_models.Room).filter(db_models.Room.room_id == room.room_id).first()
        if room.status=='SERVING':
            if room.fan_speed=='high':
                room.total_cost+=1
                room.current_temperature-=1
                db_room.current_temperature-=1
                db_room.total_cost+=1
            elif room.fan_speed=='medium':
                room.total_cost+=0.5
                room.current_temperature-=0.5
                db_room.current_temperature-=0.5
                db_room.total_cost+=0.5
            else:
                room.total_cost+=0.3
                room.current_temperature-=0.3
                db_room.current_temperature-=0.3
                db_room.total_cost+=0.3
            if room.current_temperature<=room.target_temperature:
                room.total_cost-=(room.target_temperature-room.current_temperature)
                room.current_temperature=room.target_temperature
                room.status='SLEEPING'
                db_room.status='SLEEPING'
                db_room.total_cost=room.total_cost
                db_room.current_temperature=room.target_temperature
                # 结束一个详单
                db_record = db.query(db_models.Record).filter(db_models.Record.record_id == room.record_id).first()
                db_record.end_time=datetime.now()
                db_record.duration=room.server_time
                db_record.current_cost=room.total_cost-db_record.current_cost
                room.server_time=0
                db_room.server_time=0
                serving_rooms.remove(room)
            db.commit()
        elif room.status=='SLEEPING':
            if room.current_temperature<room.target_temperature+1:
                room.current_temperature+=0.5
                db_room.current_temperature+=0.5
                db.commit()
            if room.current_temperature>=room.target_temperature+1:
                if len(serving_rooms)<3:
                    serving_rooms.append(room)
                    room.status='SERVING'
                    db_room.status='SERVING'
                    # 新建一个详单
                    db_record = db_models.Record(room_id=room.room_id, request_time=datetime.now(),start_time=datetime.now(),fan_speed=room.fan_speed,current_cost=room.total_cost)
                    #写入数据库
                    db.add(db_record)
                    db.commit()
                    db_room.record_id=db_record.record_id
                    room.record_id=db_record.record_id
                    db.commit()
                else:
                    pending_rooms.append(room)
                    room.status='WAITING'
                    db_room.status='WAITING'
                    # 新建一个详单
                    db_record = db_models.Record(room_id=room.room_id, request_time=datetime.now(), fan_speed=room.fan_speed,current_cost=room.total_cost)
                    #写入数据库
                    db.add(db_record)
                    db.commit()
                    db_room.record_id=db_record.record_id
                    room.record_id=db_record.record_id
                    db.commit()
        elif room.status=='SHUTDOWN':
            if(room.current_temperature<room.initial_temperature):
                room.current_temperature+=0.5
                db_room.current_temperature+=0.5
                if(room.current_temperature>room.initial_temperature):
                    room.current_temperature=room.initial_temperature
                    db_room.current_temperature=room.initial_temperature
            db.commit()


def power_on(db):
    schedule(db)
    calculate_cost(db)
    timer=threading.Timer(10,poweron,args=(db,))    
    timer.start()


@router.get("/poweron")
def poweron(db: Session = Depends(get_db)):
    power_on(db)
    return {"msg": "开机成功"}

class RoomData:
    def __init__(self, db_room):
        self.room_id=db_room.room_id
        self.record_id=db_room.record_id
        self.identity_card=db_room.identity_card
        self.initial_temperature=db_room.initial_temperature
        self.current_temperature=db_room.current_temperature
        self.target_temperature=db_room.target_temperature
        self.fan_speed=db_room.fan_speed
        self.status=db_room.status
        self.server_time=db_room.server_time
        self.total_cost=db_room.total_cost

# 开机请求
@router.post("/request_on")
def request_on(room_id: int,db: Session = Depends(get_db)):
    global serving_rooms,pending_rooms,all_rooms
    flag=1
    for room in all_rooms:
        if room.room_id==room_id:
            # 新建一个详单
            db_record = db_models.Record(room_id=room_id, request_time=datetime.now(), fan_speed=room.fan_speed,current_cost=room.total_cost)
            db_room=db.query(db_models.Room).filter(db_models.Room.room_id == room_id).first()
            flag=0
            if len(serving_rooms)<3:
                serving_rooms.append(room)
                room.status='SERVING'
                db_room.status='SERVING'
                db_record.start_time=datetime.now()
            else:
                pending_rooms.append(room)
                room.status='WAITING'
                db_room.status='WAITING'
            #写入数据库
            db.add(db_record)
            db.commit()
            db_room.record_id=db_record.record_id
            room.record_id=db_record.record_id
            db.commit()
    if flag==1:
        db_room = db.query(db_models.Room).filter(db_models.Room.room_id == room_id).first()
        room_data=RoomData(db_room)
        all_rooms.append(room_data)
        # 新建一个详单
        db_record = db_models.Record(room_id=room_id, request_time=datetime.now(), fan_speed=db_room.fan_speed,current_cost=db_room.total_cost)
        if len(serving_rooms)<3:
            serving_rooms.append(room_data)
            db_room.status='SERVING'
            room_data.status='SERVING'
            db_record.start_time=datetime.now()
        else:
            pending_rooms.append(room_data)
            db_room.status='WAITING'
            room_data.status='WAITING'
        #写入数据库
        db.add(db_record)
        db.commit()
        db_room.record_id=db_record.record_id
        room_data.record_id=db_record.record_id
        db.commit()
    return {"msg": "开机成功"}
        
# 关机请求
@router.post("/request_off")
def request_off(room_id: int,db: Session = Depends(get_db)):
    global serving_rooms,pending_rooms,all_rooms
    for room in all_rooms:
        if room.room_id==room_id:
            db_room = db.query(db_models.Room).filter(db_models.Room.room_id == room_id).first()

            if room.status=='SERVING':
                # 结束一个详单
                db_record = db.query(db_models.Record).filter(db_models.Record.record_id == room.record_id).first()
                db_record.end_time=datetime.now()
                db_record.duration=room.server_time
                db_record.current_cost=room.total_cost-db_record.current_cost
                room.status='SHUTDOWN'
                room.server_time=0
                db_room.status='SHUTDOWN'
                db_room.server_time=0
                serving_rooms.remove(room)

            elif room.status=='WAITING':
                room.status='SHUTDOWN'
                db_room.status='SHUTDOWN'
                pending_rooms.remove(room)
                #删除详单
                db_record = db.query(db_models.Record).filter(db_models.Record.record_id == room.record_id).first()
                db.delete(db_record)
            else:
                room.status='SHUTDOWN'
                db_room.status='SHUTDOWN'
            
            db.commit()
    return {"msg": "关机成功"}

# 调整温度请求
@router.post("/request_temp")
def request_temp(room_id: int, target_temperature: float,db: Session = Depends(get_db)):
    global serving_rooms,pending_rooms,all_rooms
    db_room = db.query(db_models.Room).filter(db_models.Room.room_id == room_id).first()
    for room in all_rooms:
        if room.room_id==room_id:
            room.target_temperature=target_temperature
            db_room.target_temperature=target_temperature
            if(room.current_temperature<=room.target_temperature):
                room.status='SLEEPING'
                db_room.status='SLEEPING'
                # 结束一个详单
                db_record = db.query(db_models.Record).filter(db_models.Record.record_id == room.record_id).first()
                db_record.end_time=datetime.now()
                db_record.duration=room.server_time
                db_record.current_cost=room.total_cost-db_record.current_cost
                serving_rooms.remove(room)
                room.server_time=0
                db_room.server_time=0
                #写入数据库
                db.add(db_record)
            db.commit()
            break
    return {"msg": "修改成功"}

# 调整风速请求
@router.post("/request_speed")
def request_speed(room_id: int, fan_speed: str,db: Session = Depends(get_db)):
    global serving_rooms,pending_rooms,all_rooms
    db_room = db.query(db_models.Room).filter(db_models.Room.room_id == room_id).first()
    db_room.fan_speed = fan_speed
    db.commit()
    for room in all_rooms:
        if room.room_id==room_id:
            room.fan_speed=fan_speed
            if room.status=='SERVING':
                # 结束一个详单
                db_record = db.query(db_models.Record).filter(db_models.Record.record_id == room.record_id).first()
                db_record.end_time=datetime.now()
                db_record.duration=room.server_time
                db_record.current_cost=room.total_cost-db_record.current_cost
                #写入数据库
                db.add(db_record)
                db.commit()
                # 新建一个详单
                db_record = db_models.Record(room_id=room.room_id, request_time=datetime.now(),start_time=datetime.now(),fan_speed=room.fan_speed,current_cost=room.total_cost)
                #写入数据库
                db.add(db_record)
                db.commit()
                db_room.record_id=db_record.record_id
                room.record_id=db_record.record_id
                db.commit()
            if room.status=='WAITING':
                # 更新一个详单
                db_record = db.query(db_models.Record).filter(db_models.Record.record_id == room.record_id).first()
                db_record.fan_speed=fan_speed
                #写入数据库
                db.commit()
            break
    return {"msg": "修改成功"}

# 返回当前队列信息
@router.get("/show")
def show(db: Session = Depends(get_db)):
    global serving_rooms,pending_rooms,all_rooms
    # 返回房间id
    service_id_list=[]
    for room in serving_rooms:
        service_id_list.append(room.room_id)
    # 返回房间id
    waiting_id_list=[]
    for room in pending_rooms:
        waiting_id_list.append(room.room_id)
    
    return service_id_list,waiting_id_list

