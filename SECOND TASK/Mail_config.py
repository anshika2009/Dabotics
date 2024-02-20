from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config["MAIL_USERNAME"] = 'evilspawn2316@gmail.com'          #give your Email id
app.config['MAIL_PASSWORD'] = 'password'              #give your email password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'evilspawn2316@gmail.com', recipients = ['anshikarjan@gmail.com'])
   msg.body = "Hello sonal my first mail app"
   mail.send(msg)
   return "Mail Sent please check"

if __name__ == '__main__':
   app.run(debug = True)