class Scheduler:
    def __init__(self) -> None:
        self.mode = 'cold'
        self.fee_rate = 1.0
        self.temp_section = [18,26,26,30]
        self.default_temp = 26
        self.schedule_num = 3
        self.total_num = 4

    def set_para(self,mode,fee_rate,temp_section,default_temp,schedule_num):
        self.mode = mode
        self.fee_rate = fee_rate
        self.temp_section = temp_section
        self.default_temp = default_temp
        self.schedule_num = schedule_num