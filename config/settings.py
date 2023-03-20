from datetime import timedelta

DEBUG = True
SECRET_KEY = '2356bea1d2fb9ef6c1076acd2f6eed47'

# email configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT =  587
MAIL_USE_TLS =  True
MAIL_USE_SSL =  False
MAIL_DEBUG =  DEBUG
MAIL_SENDER =  "abdelrahmanaboneda@gmail.com"

# celery configuration
CELERY_BROKER_URL = "redis://:aboneda_dev_password@redis:6379/0"  # 0: default database name
CELERY_RESULT_BACKEND = "redis://:aboneda_dev_password@redis:6379/0"
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_BROKER_URL = "json"
CELERY_BROKER_URL = "json"
CELERY_REDIS_MAX_CONNECTIONS = 5 # DEFAULT no limit

# sqlalchemy database
SQLALCHEMY_DATABASE_URI = ""
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User
SEED_ADMIN_EMAIL = 'abdelrahmanaboneda@gmail.com'
SEED_ADMIN_PASSWORD = 'aboneda'
# REMEMBER_COKKIE_DURATION = timedelta(days=50)
# PERMANENT_SESSION_LIFETIME = timedelta(seconds=50)
