from flask import Flask
from app.blueprints.main import main as main_blueprint
from app.blueprints.contact import contact as contact_blueprint
from app.blueprints.auth import auth as auth_blueprint
from celery import Celery
from .extensions import debug_toolbar, mail,login_manger, db, custom_bcrypt

## Celery Configuration
CELERY_TASK_LIST = ['app.blueprints.contact.tasks']

def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery(
                    app.import_name,
                    broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
    

def create_app():

    app = Flask('__name__', instance_relative_config=True,static_folder='static')

    # configuration
    app.config.from_object('config.settings') # global config
    app.config.from_pyfile('settings.py',silent=False) # secret config , it will automatically look for it in instance folder, silent = True >> it wont raise an exception if the file doesn't exist
    
    # extensions
    login_manger.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    # login configs
    login_manger.login_view = 'login'
    login_manger.login_message = 'You have to Login first to access the website'
    login_manger.login_message_category = 'warning'
    debug_toolbar.init_app(app)
    custom_bcrypt.init_app(app)
    # blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(contact_blueprint)
    app.register_blueprint(auth_blueprint)

    return app



