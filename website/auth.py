from flask import Blueprint,render_template,request,redirect,flash, url_for
from .models import User ,Note
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required, logout_user, current_user

auth = Blueprint('auth',__name__)



@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email'] 
        password = request.form.get("password") 

        user = User.query.filter_by(email=email).first()
        if user :
            if check_password_hash(user.password,password):
                flash('Logged in successfully',category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect Password,please try again.",category="error")
        else:
            flash("Uh Oh User doesn\'t exist, Please Sign Up",category="error")

    return render_template("login.html",user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))

@auth.route("/sign-up",methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form['email']
        first_name = request.form['name']
        last_name = request.form['last_name']
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Uh Oh ... User already exist",category="error")
        else:
            if len(email) < 4 :
                flash('email must be greater than 4 characters.' , category="error")
            elif len(first_name) < 1:
                flash('First Name must be greater than 1 characters.' , category="error")
            elif len(last_name) < 1:
                flash('Last Name must be greater than 1 characters.' , category="error")
            elif password != confirm_password:
                flash('Oh No Your Passwords Don\'t Appear To Match.' , category="error")
            elif len(password) < 7:
                flash(' Your password must be at least 7 characters long, contain letters and numbers, and must not contain spaces or emojis.' , category="error")
            else :
                # adding a user to db
                new_user = User(email=email,first_name=first_name,last_name=last_name,password=generate_password_hash(password,method="sha256"))
                db.session.add(new_user)
                db.session.commit()
                # login_user(user, remember=True)
                flash('Account Created Successfully',category='success')
                return redirect(url_for("views.home"))

            
    return render_template("signup.html",user=current_user)