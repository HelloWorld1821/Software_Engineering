## 后端运行方法
- `pip install fastapi[all]` : 安装fastapi
- `pip install uvicorn[standard]` : 安装uvicorn
  然后使用以下命令运行main.py
- `uvicorn main:app --reload` 

  在浏览器地址栏后加上“/docs”即可查看接口文档，例：
- `http://127.0.0.1:8000/docs` 
