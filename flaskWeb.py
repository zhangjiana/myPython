# -*- coding: utf-8 -*-
import sys

# 变量命名含义
#_username 不希望被外部调用


reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, jsonify, request, render_template

# 取模块名字
app = Flask(__name__)


@app.route('/')
def hello_world():
    # 生成的error
    # raise ValueError, "This is a error"
    return 'index Page'


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/api/book/<id>')
def api_get_book(id):
    if not id.isdigit():
        result = jsonify({"code": 1, "message": 'Params id format Error'})
        return result
    id = int(id)
    books = {
        1: "A python book",
        2: 'two python book'
    }
    return 'books is {0}'.format(books.get(id, 'not FOUND'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print 123
        username = request.form['username']
        password = request.form['password']

        users = {
            'abc': '123',
            'qwe': '456'
        }
        if not username or not password:
            return jsonify({
                "code": '1',
                "message": 'Params username or password is not Found'
            })

        if username not in users:
            return jsonify({
                "code": '1',
                "message": 'username is not Found'
            })
        if password not in users.get(username, None):
            return jsonify({
                "code": '1',
                "message": 'password is not correct'
            })
        return jsonify({
            "code": '0',
            "message": 'login success'
        })
    return render_template('login.html', username='asdf', data=[1, 2, 3, 4])


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
