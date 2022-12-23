import mysql
from flask import Flask, request, render_template

from test2.DB_unit import DB

app = Flask(__name__)


# 首页
@app.route('/', methods=['GET', 'POST'])
def home():
    # return '<h1>Home</h1><p><a href="/login">去登录</a></p>'
    return render_template("home.html")


# @app.route('/login', methods=['GET'])
# def login():
#     # return '''<form action="/login" method="post">
#     #              <p>用户名：<input name="username"></p>
#     #              <p>密码：<input name="password" type="password"></p>
#     #              <p><button type="submit">登录</button></p>
#     #              </form>'''
#     return render_template("login.html")


# 登录页处理
@app.route('/login', methods=['post','get'])
def do_login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # 从request对象读取表单内容：
        param = request.form
        db = DB(host='119.91.23.180', user='root', password='HE123456', database='test')
        sql = 'select * from users where username=' + param['username'] + ' and password=' + param['password']
        res = db.get_one(sql)
        print(request.form)
        print(res)
        if res:
            return render_template("welcome.html",username=param['username'])
        else:
            return '用户名或密码不正确。'


if __name__ == '__main__':
    app.run('', 5000)
