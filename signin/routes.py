from signin import app, db
from signin.models import Usuario
from signin.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, session, flash, redirect, url_for, request


# Routes
@app.route("/register.html", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()

    if request.method == "POST":
        username_to_login = Usuario.query.filter_by(username=form.username.data).first()
        email_to_login = Usuario.query.filter_by(email=form.email.data).first()
        if username_to_login:
            flash(f"Username: '{form.username.data}' already exists.", category="danger")
        elif email_to_login:
            flash(f"Email: '{form.email.data}' is already in use.", category="danger")
        else:
            crear_usuario = Usuario( nombre=form.nombre.data,
                                     username=form.username.data,
                                     email=form.email.data,
                                     passw=form.password.data )
            db.session.add(crear_usuario)
            db.session.commit()
            login_user(crear_usuario)
            flash(f"User created successfully.", category="success")
            flash(f"Welcome {crear_usuario.username}!", category="success")
            return redirect(url_for("login_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"{err_msg}", category="danger")
    return render_template("/register.html", form=form)
  
@app.route("/login.html", methods=["GET", "POST"])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        user_to_login = Usuario.query.filter_by(email=form.email.data).first()
        if user_to_login and user_to_login.check_password(password=form.password.data):
            login_user(user_to_login)
            flash(f"Hi {user_to_login.username} nice to see you back!", category="success")
            return redirect(url_for("login_page"))
        else:
            flash("Sorry, your email or password was incorrect. Please double-check it.", category="danger")
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"{err_msg}", category="danger")
    return render_template("/login.html", form=form)


# Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404