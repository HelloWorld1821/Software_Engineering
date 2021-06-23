from app import *
from flask import request, jsonify
from database import *
from sqlalchemy import func
import utils


# 这个暂时不用写
@app.route('/auth/loginAdmin', methods=['POST'])
def login_admin():
    """
    userName
    password
    :return:
    """
    params = request.get_json(force=True)
    
    print(request.path, " : ", params)
    return jsonify({'error': False})


# FINISH
@app.route('/auth/login', methods=['POST'])
def login():
    """
    登录
    :params:{
        username:str
        password:str
    }
    :return:{
        error: bool # 处理请求过程中是否发生错误，登录失败返回True，登录成功返回False
        type: str   # 类型:{'receptionist','manager','administrator','room'}
    }
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    username = params['username']
    password = params['password']
    print(username, ',', password)
    query_list = [
        User.username == username,
        User.password == password
    ]
    ans = User.query.filter(*query_list).first()

    if ans is None:
        return jsonify({'error': True})
    else:
        return jsonify({'error': False, 'type': ans.type})
    

# FINISH
@app.route('/receptionist/getRDR', methods=['POST'])
def create_RDR():
    """前台开详单
    roomId:int
    :return: { record:{
                    startTime:str,
                    endTime:str,
                    speed:str,
                    fee:double } ,
                error:bool}
                
    """

    params = request.get_json(force=True)
    print(request.path, " : ", params)
    roomId=params['roomId']
    times_used = User.query.filter(User.room_id == roomId).first().times_used
    ans = Room.query.filter(Room.room_id == roomId).filter(Room.times_used == times_used).all()

    start_time_list = []
    end_time_list = []
    speed_list = []
    fee_list = []
    for i in ans:
        start_time_list.append(i.start_time)
        end_time_list.append(i.end_time)
        speed_list.append(i.speed)
        fee_list.append(i.fee)

    return jsonify({'error': False,
                    'RDR': {'startTime': start_time_list,
                               'endTime': end_time_list,
                               'speed': speed_list,
                               'fee': fee_list}})


# FINISH
@app.route('/receptionist/getBill', methods=['POST'])
def create_bill():
    """前台开账单
    roomId:int
    :return: { fee:double ,
                error:bool }
    """

    params = request.get_json(force=True)
    print(request.path, " : ", params)
    roomId=params['roomId']
    times_used = User.query.filter(User.room_id == roomId).first().times_used
    fee = db.session.query(func.sum(Room.fee)).filter(Room.room_id == roomId).filter(Room.times_used == times_used).scalar()
    if fee is None:
        fee = 0

    return jsonify({'error': False,
                    'bill': {'fee': fee}})


# FINISH
@app.route('/receptionist/checkIn', methods=['POST'])
def check_in():
    """前台开房
    roomId
    :return: { idCard:str ,
                error:bool }
    """
    params = request.get_json(force=True)
    # print(request.path, " : ", params)
    roomId = params['roomId']
    # print(username, ',', password)
    query_list = [
        User.room_id == roomId,
        User.status == 'out'
    ]
    ans = User.query.filter(*query_list).first()

    if ans is None:
        return jsonify({'error': True})
    else:
        idCard = utils.random_str()
        User.query.filter(*query_list).update({
            'status':'in',
            'times_used':ans.times_used+1,
            'password':idCard
        })
        db.session.commit()
        return jsonify({'error': False, 'idCard': idCard})


# FINISH
@app.route('/receptionist/checkOut', methods=['POST'])
def check_out():
    """前台退房
    roomId:int
    :return: { error:bool }
    """

    params = request.get_json(force=True)
    # print(request.path, " : ", params)
    roomId = params['roomId']
    # print(username, ',', password)
    query_list = [
        User.room_id == roomId,
        User.status == 'in'
    ]
    ans = User.query.filter(*query_list).first()

    if ans is None:
        return jsonify({'error': True})
    else:
        User.query.filter(*query_list).update({
            'status':'out',
        })
        db.session.commit()
        return jsonify({'error': False})


@app.route('/manager/checkReport', methods=['POST'])
def check_report():
    """经理生成格式化报表
    startTime:str
    endTime:str
    :return: { error:bool,
                report:{ totalNum:int , 使用空调次数
                        commonTemp:int , 最常使用的温度
                        commonSpeed:str , 最常使用的风速
                        satisfyNum:int , 到达目标温度的次数
                        scheduledNum:int, 被调度的次数
                        RDRNum:int , 生成RDR的次数
                        totalFee:double }}
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({'error': False,
                    'report': {'totalNum': 20,
                               'commonTemp': 23,
                               'commonSpeed': 'mid',
                               'satisfyNum': 10,
                               'scheduledNum': 30,
                               'RDRNum': 25,
                               'totalFee': 12450.0
                               }})


@app.route('/administrator/setDefaultParams', methods=['POST'])
def set_default_params():
    """管理员设置默认参数
    mode:str
    tempSection:int[4]
    defaultTemp: int
    feeRate: double
    scheduleNum: int
    :return: {error:bool}
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({'error': False})


@app.route('/administrator/checkRoomState', methods=['POST'])
def check_room_state():
    """管理员检查房间状态
    :return: { roomStates:[ roomState:
                           {roomId:int,
                            isCheckIn:bool,
                            mode:str,
                            speed:str,
                            currTemp:int,
                            targetTemp:int
                            }],
                            error:bool }
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({'error': False,
                    'roomStates': [{'roomState': {'roomId': 1,
                                                  'isCheckIn': False,
                                                  'mode': 'hot',
                                                  'speed': 'low',
                                                  'currTemp': 23,
                                                  'targetTemp': 25}},
                                   {'roomState': {'roomId': 2,
                                                  'isCheckIn': False,
                                                  'mode': 'cold',
                                                  'speed': 'high',
                                                  'currTemp': 26,
                                                  'targetTemp': 5}},
                                   {'roomState': {'roomId': 3,
                                                  'isCheckIn': True,
                                                  'mode': 'hot',
                                                  'speed': 'mid',
                                                  'currTemp': 12,
                                                  'targetTemp': 15}}
                                   ]})


@app.route('/room/getRoomState', methods=['POST'])
def get_room_state():
    """
    客户定期请求空调信息
    :params:{
        roomId:int          # 房间号
        cookie ?            # 这玩意儿我不是很懂，我这边暂时不打算用
    }
    :return: {
        roomState:{
            speed:str,      # 风速：{"High", "Medium", "Low"}
            currTemp:int,   # 当前温度
            targetTemp:int, # 目标温度
            fee:double,     # 费用
            acState:str     # 空调状态：{"On","Off","WaitForSchedul","Sleep"}
        },
        error:bool          # 处理请求过程是否发生错误，一般回送False
    }
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({
        'error': False,
        'roomState': {
            'speed': 'high',
            'currTemp': 15,
            'targetTemp': 25,
            'fee': 103.2,
            'acState': 'on'
        }
    })


@app.route('/room/changeRoomState', methods=['POST'])
def change_room_state():
    """
    客户发送开关机、送风、调温请求
    params:{
        roomId:int,         # 房间号
        targetTemp:int,     # 目标温度
        targetSpeed:str,    # 目标风速：{"High", "Medium", "Low"}
        acState:str         # 开机/关机：{"On", "Off"}
    }
    :return: {
        error:bool          # 处理请求过程是否发生错误，一般回送False
    }
    """
    params = request.get_json(force=True)
    roomId = params['roomId']
    targetTemp = params['targetTemp']
    targetSpeed = params['targetSpeed']
    acState = params['acState']
    print(request.path, " : ", params)
    return jsonify({
        'error': False
    })


@app.route('/')
def hello_world():
    print(request.path)
    print(request.full_path)
    return "hello"


if __name__ == '__main__':
    # db_init()  # 这行代码，如果数据库没有发生变化，则跑一次即可
    app.run(port=5000, debug=True, host='0.0.0.0')