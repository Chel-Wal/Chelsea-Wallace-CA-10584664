from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template("LogIn.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Log Out</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
     if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstname) < 2:
            flash('Please Enter A valid First Name Must Be Greater Than 1 Character', category='error')
        elif len(lastname) < 2:
            flash('Please Enter A valid Last Name Must Be Greater Than 1 Character', category='error')
        elif len(email) < 4:
            flash('Please Enter A Valid Email', category='error')
        elif password1 != password2:
            flash('Passwords Don\'t Match', category='error')
        elif len(password1) < 7:
            flash('Password Must Be At Least 7 Characters', category='error')
        else:
            flash('Account Created!', category='success')
            
            
     return render_template("sign_up.html")



