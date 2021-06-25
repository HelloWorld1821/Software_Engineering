from app import *

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), nullable=True)
    type = db.Column(db.Enum('receptionist','manager','administrator','room'))
    times_used = db.Column(db.Integer, default=0)
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
    
    db.session.commit()