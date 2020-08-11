from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from forms import ContactForm
app = Flask(__name__)

app.secret_key = 'development key'

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'elhussenportfoliocontact@gmail.com'
app.config['MAIL_PASSWORD'] = 'alahakbr12'
app.config['MAIL_DEFAULT_SENDER'] = 'elhussenportfoliocontact@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.message.data
        subject = form.subject.data
        email = form.email.data
        msg = Message(recipients=["alhoseenemad@gmail.com"],
        body='from : %s <%s>\n\n%s'%(name, email, body),
        subject=subject)    
        mail.send(msg)
        print('Message sent!')
        return redirect('/')
    return render_template('index.html', form=form)


app.run()