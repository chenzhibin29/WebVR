# coding:utf-8

from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/index', methods=['post', ])
def login():
    name = request.form.get('Username')
    password = request.form.get('Password')

    # print(name,password)
    if name == 'admin' and password == 'admin':
        return render_template('index.html')
    return '输入有误'


@app.route('/back_index', methods=['post', 'get'])
def back_index():
    return render_template('index.html')


@app.route('/car', methods=['post', 'get'])
def get_form():
    return render_template('car.html')


@app.route('/car/car1', methods=['post', 'get'])
def get_form2():
    return render_template('car1.html')


@app.route('/dianji', methods=['post', 'get'])
def get_form1():
    return render_template('dianji.html')


#  @app.errorhandler(404)
#  def page_not_found(error):
# return render_template('404.html'),404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
