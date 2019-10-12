from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('mobile.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print("User:%s ---- Password:%s" % (username, password))
        if all([username, password]):
            if password == "411324":
                flash('Login Successfully.')
            else:
                flash('username or password error!')
        else:
            flash("用户名或密码不能为空")
        return render_template('m.html')
@app.route('/index')
def index():
    url = 'http://www.baidu.com'
    return render_template('index.html', search=url)


@app.route('/number/<ID>')
def discovery(ID):
    return "Client ID : %s" % ID


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
