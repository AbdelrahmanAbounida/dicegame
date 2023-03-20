from app.extensions import db 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous.url_safe import URLSafeTimedSerializer
from flask import current_app
from collections import OrderedDict
from .utils import ResourceMixin, AwareDataTime
from app.extensions import login_manger

class User(UserMixin, ResourceMixin, db.Model):

    ROLE = OrderedDict([
        ('member','Member'),
        ('admin','Admin')
    ])
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)

    # Authentication
    role = db.Column(db.Enum(*ROLE, name='role_types',native_enum=False),index=True,nullable=False,server_default='member')
    active = db.Column('is_active',db.Boolean(),nullable=False,server_default='1')
    username = db.Column(db.String(50),nullable=True)
    email = db.Column(db.String(200),nullable=False,unique=True,server_default='')
    password = db.Column(db.String(100),nullable=False,server_default='')

    # Activity Tracking
    sign_in_count = db.Column(db.Integer, default=0)
    current_sign_in_ip = db.Column(db.String(45))
    last_sign_in_ip = db.Column(db.String(45))
    current_sign_in_on = db.Column(AwareDataTime())
    last_sign_in_on = db.Column(AwareDataTime())

@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

   