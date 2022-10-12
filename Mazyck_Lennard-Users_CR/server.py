from flask import Flask, request, render_template, redirect, session
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users = users)

@app.route('/new_user')
def new_user():
    return render_template('new_user.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return redirect('/')

@app.route('/delete/<int:user_id>/user')
def destroy(user_id):
    data = {
        'id' : user_id
    }
    User.destroy(data)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)