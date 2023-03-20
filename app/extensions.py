from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manger = LoginManager()
debug_toolbar = DebugToolbarExtension()
mail = Mail()
custom_bcrypt = Bcrypt()
