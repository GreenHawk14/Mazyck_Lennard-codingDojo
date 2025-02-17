from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.models_user import User
from flask_app.config.mysqlconnection import connectToMySQL


@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users = users)

@app.route('/new_user')
def new_user():
    return render_template('new_user.html')

#Add a new User
@app.route('/create_user', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return redirect('/')

#Removes a User
@app.route('/delete/<int:user_id>/user')
def destroy(user_id):
    data = {
        'id' : user_id
    }
    User.destroy(data)
    return redirect('/')

#Edit selected user information
#Displays information
@app.route("/edit/<int:user_id>")
def editUser(user_id):
    data = {
        'id' : user_id
    }
    user = User.get_one(data)
    return render_template('edit_user.html', user = user)

#Update user information
@app.route("/update/<int:user_id>", methods=['POST'])
def updateUser(user_id):
    data = {
        'id' : user_id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.update(data)
    return redirect('/')
