from enum import unique
from flask import Flask, config, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), nullable=True)
    type = db.Column(db.Enum('receptionist','manager','administrator','room'))

    def __repr__(self) -> str:
        return '{0},{1},{2},{3}'.format(self.id,self.username,self.password,self.type)

def db_init():
    db.drop_all()
    db.create_all()
    db.session.add(User(username='receptionist_1',password='receptionist',type='receptionist'))
    db.session.add(User(username='manager_1',password='manager',type='manager'))
    db.session.add(User(username='administrator_1',password='administrator',type='administrator'))
    db.session.add(User(username='room_1',password='room',type='room'))
    db.session.commit()







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
    ans = User.query.filter(User.username == username and User.password == password).first()

    if ans is None:
        return jsonify({'error': True})
    else:
        return jsonify({'error': False, 'type': ans.type})
    


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
    print(request.path, " : ", params)
    return jsonify({
        'error': False
    })


@app.route('/')
def hello_world():
    print(request.path)
    print(request.full_path)
    return request.args.__str__()


if __name__ == '__main__':
    # db_init()  # 这行代码跑一次即可
    app.run(port=5000, debug=True, host='0.0.0.0')
