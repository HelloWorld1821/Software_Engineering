<!--
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 20:40:55
 * @LastEditors: l
 * @LastEditTime: 2021-06-04 16:00:23
 * @FilePath: \DistributedControlSystem\README.md
-->
# DistributedControlSystem
一个酒店分布式温控系统，前端采用Vue + Element ,后端使用Flask
## 前端运行方法
- `npm install` : 安装依赖
- `npm run dev` : 启动服务器
## 后端运行方法
- `pip install -r requirements.txt` :创建虚拟环境
- 数据库初始化

  第一次运行时请运行main函数中的db_init()来初始化数据库。
  数据库相关配置在config.py中，建议你在本地mysql创建一个名为air，密码为123456的用户，并授予所有权限。同时创建一个名为air的数据库。
- `python main.py`：启动服务器
## 运行效果
### 主界面
![image](https://user-images.githubusercontent.com/54203997/123535202-fa360100-d754-11eb-8c8f-b2d4b9a13426.png)
### 登录界面
![image](https://user-images.githubusercontent.com/54203997/123535213-06ba5980-d755-11eb-89ad-acf86894e519.png)

### 用户界面
![image](https://user-images.githubusercontent.com/54203997/123535179-e25e7d00-d754-11eb-878a-b84900daf36e.png)

### 前台界面
![image](https://user-images.githubusercontent.com/54203997/123535228-189bfc80-d755-11eb-8257-d68855c3f858.png)

### 经理界面
![image](https://user-images.githubusercontent.com/54203997/123535238-29e50900-d755-11eb-9376-3c60439c21da.png)

### 管理员界面
![image](https://user-images.githubusercontent.com/54203997/123535264-4c772200-d755-11eb-82f2-f399b19fa2ad.png)


