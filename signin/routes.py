import io, base64
from signin import app, db
from signin.models import User
from signin.forms import RegisterForm, LoginForm, ResetPasswordForm
from signin.scraper import getQuotation
from flask_login import login_user
from flask import render_template, flash, redirect, url_for, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Routes
@app.route("/")
@app.route("/python-flask-signin/home.html", methods=["GET"])
def home_page():
    if request.method == "GET":
        df = getQuotation()
        
        # Generate plot
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("U$D")
        axis.set_xlabel("Date")
        axis.set_ylabel("Value")
        axis.grid()
        axis.plot(range(130,330,10), "ro-")
    
        # Convert plot to PNG image
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)

        # Encode PNG image to base64 string
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template( "/home.html", 
                            column_names=df.columns.values, 
                            row_data=list(df.values.tolist()),
                            zip=zip, image=pngImageB64String
                          )

@app.route("/python-flask-signin/register.html", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()

    if request.method == "POST" and form.validate():
        username_to_register = User.query.filter_by(username=form.username.data).first()
        email_to_register = User.query.filter_by(email=form.email.data).first()
        if username_to_register:
            flash(f"'{form.username.data}' already exists.", category="danger")
        elif email_to_register:
            flash(f"'{form.email.data}' is already in use.", category="danger")
        else:
            crear_usuario = User(   full_name=form.nombre.data,
                                    username=form.username.data,
                                    email=form.email.data,
                                    passw=form.password.data )
            db.session.add(crear_usuario)
            db.session.commit()
            login_user(crear_usuario)
            flash(f"User created successfully.", category="success")
            return redirect(url_for("login_page"))    
    return render_template("/register.html", form=form)
  
@app.route("/python-flask-signin/")
@app.route("/python-flask-signin/login.html", methods=["GET", "POST"])
def login_page():
    form = LoginForm()

    if request.method == "POST" and form.validate():
        user_to_login = User.query.filter_by(email=form.email.data).first()
        if user_to_login is None:
            flash(f"The email you entered doesn't belong to an account. Please check your email and try again.", category="danger")
        elif user_to_login.check_password(password=form.password.data):
            login_user(user_to_login)
            flash(f"Hi {user_to_login.username} nice to see you back!", category="success")
            return redirect(url_for("login_page"))
        else:
            flash("Sorry, your password was incorrect. Please double-check your password.", category="danger")
    return render_template("/login.html", form=form)

@app.route("/python-flask-signin/forgot_password.html", methods=["GET", "POST"])
def reset_password_page():
    form = ResetPasswordForm()
    if request.method == "POST" and form.validate():
        user_to_login = User.query.filter_by(email=form.email.data).first()
        if user_to_login is None:
            flash(f"The email you entered doesn't belong to an account.", category="danger")
        else:
            flash("Email sent. Please follow the steps in the email.", category="success")
    return render_template("/forgot_password.html", form=form)

# Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404