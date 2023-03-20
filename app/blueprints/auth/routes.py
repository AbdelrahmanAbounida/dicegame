from flask import render_template, request, flash, redirect
from flask_login import login_required, logout_user, current_user, login_user
from . import auth 
from .models import User 
from .forms import LoginForm, RegisterForm
from app.extensions import custom_bcrypt

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            print(user)
            print(password)
            if user and custom_bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user)
                return redirect('/')
            else:
                flash('Login unsuccessful. Please Check your email or password','danger')
        else:
            print("Form validation Failed")
    
    print("GET")

    return render_template('auth/login.html',form=form)


@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # retrieve form data
            username = form.username.data
            email = form.email.data
            password = custom_bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            # add to database

            user = User.query.filter_by(email=email).first()

            if user:
                flash('User with the same email already exist', 'danger')
                return redirect('/register')
             
            user = User(email=email,password=password)
            user.save()
            flash(f'Account Created for {form.username.data}','success')
            return redirect('/')
        else:
            print("no")
    return render_template('auth/register.html',form=form)

@auth.route('/forgetPassword',methods=['GET','POST'])
def forgetPassword():
    form = RegisterForm()
    return render_template('auth/forgetPassword.html')

@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

