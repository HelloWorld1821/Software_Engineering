from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


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


@app.route('/auth/login', methods=['POST'])
def login():
    """

    :return:
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({'error': False})


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
    return jsonify({'error': False,
                    'record': {'startTime': '2021-6-2,15:20',
                               'endTime': '2021-6-3,16:40',
                               'speed': 'high',
                               'fee': 2333.3}})


@app.route('/receptionist/getBill', methods=['POST'])
def create_bill():
    """前台开账单
    roomId:int
    :return: { fee:double ,
                error:bool }
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({'error': False,
                    'fee': 123.3})


@app.route('/receptionist/checkIn', methods=['POST'])
def check_in():
    """前台开房
    roomId
    :return: { idCard:str ,
                error:bool }
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({'error': False,
                    'idCard': 'asdfjk42dfsd'})


@app.route('/receptionist/checkOut', methods=['POST'])
def check_out():
    """前台退房
    roomId:int
    :return: { error:bool }
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
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


@app.route('/administrator/checkRoomsState', methods=['POST'])
def check_room_state():
    """管理员检查房间状态

    :return: { roomsStates:[ roomState:
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
                    'roomsState': [{'roomState': {'roomId': 1,
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


@app.route('/room/updateRoomState', methods=['POST'])
def update_room_state():
    """
    roomId:int
    :return: { roomState:{  speed:str,
                            currTemp:int,
                            targetTemp:int,
                            fee:double,
                            acState:str},
                            error:bool}
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({'error': False,
                    'roomState': {'speed': 'high',
                                  'currTemp': 15,
                                  'targetTemp': 25,
                                  'fee': 103.2,
                                  'acState': 'on'}})


@app.route('/room/changeRoomState', methods=['POST'])
def change_room_state():
    """
    roomId:int,
    targetTemp:int,
    targetSpeed:str,
    acState:str
    :return: { error:bool }
    """
    params = request.get_json(force=True)
    print(request.path, " : ", params)
    return jsonify({'error': False})


@app.route('/')
def hello_world():
    print(request.path)
    print(request.full_path)
    return request.args.__str__()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
