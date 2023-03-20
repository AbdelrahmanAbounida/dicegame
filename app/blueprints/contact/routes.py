from . import contact
from flask_mail import Message
from app.extensions import mail
from .forms import EmailForm
from flask import request, flash, render_template

@contact.route('/contact', methods=['GET', 'POST'])
def contact():
	form = EmailForm()
	from .tasks import sendContactEmail # prevent circular routing , wait until the app get initalized

	if request.method == "POST":
		if form.validate_on_submit():
			email = form.email.data
			message = form.message.data

			sendContactEmail(email,message)
			
			flash("We have Recieved Your Message, will get back soon","success")
		else:
			print("Form not valid")
	
	return render_template('email/contact.html',form=form)
	