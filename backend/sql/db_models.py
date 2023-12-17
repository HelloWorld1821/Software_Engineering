from sqlalchemy import Boolean, Column, ForeignKey, Integer,Float, String, Enum, DateTime
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL="sqlite:///./sql_app.db"

engine=create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

#Room（房间）表格
class Room(Base):
    __tablename__='rooms'

    room_id=Column(Integer, primary_key=True, unique=True, index=True, info={'description': '房间号'})
    record_id=Column(Integer, ForeignKey('records.record_id'), nullable=True, index=True, info={'description': '详单记录号'})
    identity_card=Column(String, info={'description': '身份证号(密码)'})
    initial_temperature=Column(Float, info={'description': '房间初始温度'})
    current_temperature=Column(Float, info={'description': '当前温度'})
    target_temperature=Column(Float, default=25.0, info={'description': '目标温度'})
    fan_speed=Column(Enum('high','medium','low'), default='medium', info={'description': '风速'})
    status=Column(Enum('SERVING', 'WAITING', 'SHUTDOWN', 'SLEEPING'), default='SHUTDOWN', info={'description': '空调状态'})
    server_time=Column(Integer, default=0, info={'description': '服务时间（以秒为单位）'})
    total_cost=Column(Float, default=0.0, info={'description': '总费用'})

#Record（详单）表格
class Record(Base):
    __tablename__='records'

    record_id=Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, info={'description': '详单记录号'})
    room_id=Column(Integer, ForeignKey('rooms.room_id'), nullable=False, index=True, info={'description': '房间号'})
    request_time=Column(DateTime, default=datetime.now(), info={'description': '请求时间'})
    start_time=Column(DateTime, info={'description': '服务开始时间'})
    end_time=Column(DateTime, info={'description': '服务结束时间'})
    duration=Column(Integer, info={'description': '服务时长'})
    fan_speed=Column(Enum('high','medium','low'), default='medium', info={'description': '风速'})
    current_cost=Column(Float, info={'description': '当前费用'})
    rate=Column(Integer, default=1, info={'description': '费率'})

#Bill（账单）表格
class Bill(Base):
    __tablename__ = 'bills'

    bill_id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, info={'description': '账单号'})
    room_id = Column(Integer, ForeignKey('rooms.room_id'), nullable=False, index=True, info={'description': '房间号'})
    checkin_time = Column(DateTime, info={'description': '入住时间'})
    checkout_time = Column(DateTime, info={'description': '退房时间'})
    total_cost = Column(Float, info={'description': '空调总费用'})

#获取数据库会话
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)