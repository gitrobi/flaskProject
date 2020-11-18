from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


@app.route('/flask')
def hello_flask():
    return 'Hello Flask'


@app.route('/python/')
def hello_python():
    return 'Hello Python'


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    print(url_for('hello_admin'), type(url_for('hello_admin')))
    if name == 'admin':
        return redirect(url_for('hello_admin'))  # 动态构建url
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/h')
def index():
    return render_template('hello.html')


@app.route("/")
def index2():
    return render_template("index.html")


@app.route('/var')
def index_var():  # 变量名称必须和html模板中定义的变量名称一致
    # 往模板中传入的数据
    my_str = 'Hello Word'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('var.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                           )


@app.route('/var2')
def index_var2():
    my_int = 18
    my_str = 'curry'
    my_list = [1, 5, 4, 3, 2]
    my_dict = {
        'name': 'durant',
        'age': 28
    }

    # render_template方法:渲染模板
    # 参数1: 模板名称  参数n: 传到模板里的数据
    return render_template('var2.html',
                           my_int=my_int,
                           my_str=my_str,
                           my_list=my_list,
                           my_dict=my_dict)


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print(type(result), result)
        return render_template("result.html", result=result)


@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("w3cshool", "w3cshool", max_age=3600)
    return resp


@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("w3cshool")  # 获取名字为Itcast_1对应cookie的值
    return cookie_1


@app.route("/del_cookies")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("w3cshool")

    return resp


@app.route('/ss')
def index_ss():
    if 'username' in session:
        username = session['username']
        return f"Logged in as  '{username}'<br> " \
               "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login_xx'></b>" \
           "click here to log in</b></a>"


app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'


@app.route('/login_xx', methods=['GET', 'POST'])
def login_xx():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index_ss'))
    return '''

   <form action = "" method = "post">
      <p><input type = "text" name = "username"/></p>
      <p><input type = "submit" value = "Login"/></p>
   </form>

   '''


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index_ss'))


@app.route('/abort')
def index1():
   return render_template('login_abort.html')

@app.route('/login_abort',methods = ['POST', 'GET'])
def login1():
   if request.method == 'POST':
      if request.form['username'] == 'admin' :
         return redirect(url_for('success1'))
      else:
         abort(401)
   else:
      return redirect(url_for('index1'))

@app.route('/success1')
def success1():
   return 'logged in successfully'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
