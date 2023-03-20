from app.extensions import mail
from flask import current_app, render_template
from app import create_celery_app
from app.extensions import mail
from flask_mail import Message

def send_template_message(subject,sender,recipients,template_name,email,message):
    msg = Message(subject=subject,sender=sender, recipients=recipients,reply_to=sender)
    msg.html = render_template(template_name,email=email,message=message)
    mail.send(msg)

## celery handling 

celery = create_celery_app(current_app)
@celery.task()
def sendContactEmail(email,message):

    subject="DiceGame Contact"
    sender="abdelrahmanaboneda@gmail.com"
    recipients=["abdelrahmanaboneda@gmail.com"] # celery.conf.get('MAIL_USERNAME')
    template_name = "email/emailTemplate.html"
    send_template_message(subject,sender,recipients,template_name,email=email,message=message)

    return None



