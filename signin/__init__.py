from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, template_folder="templates")

# Credentials
uid = "root"
passwd = "SignIn2022Root"
ip = ""
database = "signin_db"

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{uid}:{passwd}@{ip}:3306/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "14fb3188089cdac6ba30ddcb"

# SQLAlchemy
db = SQLAlchemy(app)

# Bcrypt
bcrypt = Bcrypt(app)

# Login manager
login_man = LoginManager(app)

from signin import routes