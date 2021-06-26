from app import *

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), nullable=True)
    type = db.Column(db.Enum('receptionist','manager','administrator','room'))
    times_used = db.Column(db.Integer, default=1)
    room_id = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Enum('in','out'), default='out')

    def __str__(self) -> str:
        if(self.type != 'room'):
            return 'id:{0},username:{1},password:{2},type:{3}'.format(
                self.id,self.username,self.password,self.type)
        else:
            return 'id:{0},username:{1},password:{2},type:{3},times_used{4},status:{5},room_id:{6}'.format(
                self.id,self.username,self.password,self.type,self.times_used,self.status,self.room_id)

    def __repr__(self) -> str:
        return self.__str__()

class RoomRecode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, nullable=True)
    start_time = db.Column(db.DateTime, default=datetime.datetime.now)
    end_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    speed = db.Column(db.Enum("High", "Medium", "Low"))
    fee = db.Column(db.Float, default=0.0)
    times_used = db.Column(db.Integer, nullable=True)

    def __str__(self) -> str:
        return 'id:{0},room_id:{1},start_time:{2},end_time:{3},speed:{4},fee:{5},times_used:{6}'.format(
            self.id,self.room_id,self.start_time,self.end_time,self.speed,self.fee,self.times_used)

    def __repr__(self) -> str:
        return self.__str__()

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, nullable=True)
    mode = db.Column(db.String(80))
    speed = db.Column(db.Enum("High", "Medium", "Low", "Zero"))
    current_temp = db.Column(db.Integer, nullable=True)
    target_temp = db.Column(db.Integer, nullable=True)

class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalNum = db.Column(db.Integer)

# 各种计数
class NewStatistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.DateTime, default=datetime.datetime.now)
    totalNum = db.Column(db.Integer)
    satisfyNum = db.Column(db.Integer, nullable=True)
    scheduledNum = db.Column(db.Integer, nullable=True)
    RDRNum = db.Column(db.Integer, nullable=True)
    totalFee = db.Column(db.Float, default=0.0)

    def __str__(self) -> str:
        return 'id:{0},dateTime:{1},totalNum:{2},satisfyNum:{3},scheduledNum:{4},RDRNum:{5},totalFee:{6}'.format(
            self.id,self.dateTime,self.totalNum,self.satisfyNum,self.scheduledNum,self.RDRNum,self.totalFee)

    def __repr__(self) -> str:
        return self.__str__()

class TempSpeed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateTime = db.Column(db.DateTime, default=datetime.datetime.now)
    currentTemp = db.Column(db.Integer, nullable=True)
    currentSpeed = db.Column(db.Enum("High", "Medium", "Low", "Zero"))

    def __str__(self) -> str:
        return 'id:{0},dataTime:{1},currentTemp:{2},currentSpeed:{3}'.format(
            self.id,self.dateTime,self.currentTemp,self.currentSpeed
        )
    
    def __repr__(self) -> str:
        return self.__str__()



def db_init():
    db.drop_all()
    db.create_all()
    db.session.add(User(username='receptionist_1',password='receptionist',type='receptionist'))
    db.session.add(User(username='manager_1',password='manager',type='manager'))
    db.session.add(User(username='administrator_1',password='administrator',type='administrator'))
    db.session.add(User(username='room_1',password='room',type='room',room_id=101))
    db.session.add(User(username='room_2',password='room',type='room',room_id=102))
    db.session.add(User(username='room_3',password='room',type='room',room_id=103))
    db.session.add(User(username='room_4',password='room',type='room',room_id=104))

    # 测试数据1
    db.session.add(RoomRecode(room_id=101,speed='High',fee=261,times_used=1))
    db.session.add(RoomRecode(room_id=101,speed='Low',fee=988,times_used=1))
    db.session.add(RoomRecode(room_id=101,speed='High',fee=661,times_used=2))
    db.session.add(RoomRecode(room_id=102,speed='High',fee=333,times_used=1))

    # 测试数据2
    db.session.add(Room(room_id=101,mode='cold',speed='Zero',current_temp=26,target_temp=26))
    db.session.add(Room(room_id=102,mode='cold',speed='Zero',current_temp=26,target_temp=26))
    db.session.add(Room(room_id=103,mode='cold',speed='Zero',current_temp=26,target_temp=26))
    db.session.add(Room(room_id=104,mode='cold',speed='Zero',current_temp=26,target_temp=26))

    # 测试数据3
    dates=['2021/06/23','2021/06/24','2021/06/25','2021/06/26']
    format_dates=[]
    for date in dates:
        format_dates.append(datetime.datetime.strptime(date,'%Y/%m/%d'))
    db.session.add(NewStatistics(dateTime=format_dates[0],totalNum=10,satisfyNum=25,scheduledNum=36,RDRNum=12,totalFee=15.8))
    db.session.add(NewStatistics(dateTime=format_dates[1],totalNum=20,satisfyNum=26,scheduledNum=37,RDRNum=13,totalFee=16.8))
    db.session.add(NewStatistics(dateTime=format_dates[2],totalNum=30,satisfyNum=27,scheduledNum=38,RDRNum=14,totalFee=17.8))
    db.session.add(NewStatistics(dateTime=format_dates[3],totalNum=40,satisfyNum=28,scheduledNum=39,RDRNum=15,totalFee=18.8))
    
    # 测试数据4
    dates=['2021/06/23','2021/06/24','2021/06/25','2021/06/26']
    format_dates=[]
    for date in dates:
        format_dates.append(datetime.datetime.strptime(date,'%Y/%m/%d'))
    db.session.add(TempSpeed(dateTime=format_dates[0],currentTemp=15,currentSpeed='High'))
    db.session.add(TempSpeed(dateTime=format_dates[0],currentTemp=16,currentSpeed='Low'))
    db.session.add(TempSpeed(dateTime=format_dates[0],currentTemp=16,currentSpeed='High'))

    db.session.add(TempSpeed(dateTime=format_dates[1],currentTemp=15,currentSpeed='Medium'))
    db.session.add(TempSpeed(dateTime=format_dates[1],currentTemp=16,currentSpeed='High'))
    db.session.add(TempSpeed(dateTime=format_dates[1],currentTemp=15,currentSpeed='High'))
    db.session.add(TempSpeed(dateTime=format_dates[1],currentTemp=15,currentSpeed='Low'))

    db.session.add(TempSpeed(dateTime=format_dates[2],currentTemp=15,currentSpeed='High'))
    db.session.add(TempSpeed(dateTime=format_dates[2],currentTemp=17,currentSpeed='Low'))
    db.session.add(TempSpeed(dateTime=format_dates[2],currentTemp=17,currentSpeed='Medium'))
    db.session.add(TempSpeed(dateTime=format_dates[2],currentTemp=17,currentSpeed='Medium'))

    db.session.add(TempSpeed(dateTime=format_dates[3],currentTemp=17,currentSpeed='Low'))
    db.session.add(TempSpeed(dateTime=format_dates[3],currentTemp=15,currentSpeed='High'))
    db.session.add(TempSpeed(dateTime=format_dates[3],currentTemp=17,currentSpeed='Low'))


    db.session.commit()