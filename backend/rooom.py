class Rooom:
    def __init__(self,room_id, current_temp) -> None:
        self.power = False
        self.room_id = room_id
        self.current_temp = current_temp
        self.current_speed = None
        self.target_temp = None
        self.target_speed = None
    
    # 开机
    def power_on(self):
        self.power = True
        return True

    # 关机
    def power_off(self):
        self.power = False
        return True
    
    def set_target_temp(self,target_temp):
        self.target_temp = target_temp

    def set_target_speed(self, target_speed):
        self.target_speed = target_speed
