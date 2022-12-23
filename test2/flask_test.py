import mysql
from flask import Flask, request

from test2.DB_unit import DB

app = Flask(__name__)


# 首页
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1><p><a href="/login">去登录</a></p>'


@app.route('/login', methods=['GET'])
def login():
    return '''<form action="/login" method="post">
                 <p>用户名：<input name="username"></p>
                 <p>密码：<input name="password" type="password"></p>
                 <p><button type="submit">登录</button></p>
                 </form>'''


# 登录页处理
@app.route('/login', methods=['post'])
def do_login():
    # 从request对象读取表单内容：
    param = request.form
    db = DB(host='119.91.23.180', user='root', password='HE123456', database='test')
    sql = 'select * from users where username=' + param['username'] + ' and password=' + param['password']
    res = db.get_one(sql)
    # if param['username'] == 'yjc' and param['password'] == 'yjc':
    #     return '欢迎您 %s !' % param['username']
    # else:
    #     return '用户名或密码不正确。'
    # pass
    print(res)
    if res:
        return '欢迎您 %s !' % param['username']
    else:
        return '用户名或密码不正确。'


if __name__ == '__main__':
    app.run('', 5000)
