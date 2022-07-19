from datetime import timezone
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column
from signin import db, bcrypt, login_man
from flask_login import UserMixin

@login_man.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Tables
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String(length=50), nullable=False)
    username = db.Column(db.String(length=50))
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    pwd_hash = db.Column(db.String(length=60), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    @property
    def passw(self):
        return self.passw
    
    @passw.setter
    def passw(self,password):
        self.pwd_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    
    def check_password(self,password):
        return bcrypt.check_password_hash(self.pwd_hash,password)


db.create_all()
db.session.commit()