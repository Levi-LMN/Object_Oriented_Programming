# app.py

from flask import Flask, render_template, jsonify, request
import pyotp
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'retailsysx@gmail.com'
app.config['MAIL_PASSWORD'] = 'qecs yhcc gkeq nlee'
app.config['MAIL_DEFAULT_SENDER'] = 'retailsysx@gmail.com'

mail = Mail(app)
otp_storage = {}  # Temporary storage for demonstration purposes

def generate_otp():
    return pyotp.random_base32()

def send_otp_email(email, otp):
    msg = Message('Your OTP', recipients=[email])
    msg.body = f'Your OTP is: {otp}'
    mail.send(msg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-otp', methods=['POST'])
def send_otp():
    email = request.form.get('email')
    otp = generate_otp()

    otp_storage[email] = otp  # Store OTP temporarily for verification

    print(f'Generated OTP for {email}: {otp}')

    send_otp_email(email, otp)
    return jsonify({"success": True, "message": "OTP sent successfully!"})

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    email = request.form.get('email')
    user_input = request.form.get('otp')

    stored_otp = otp_storage.get(email)

    if stored_otp and stored_otp == user_input:
        return jsonify({"success": True, "message": "Authentication successful!"})
    else:
        return jsonify({"success": False, "message": "Authentication failed."})

if __name__ == '__main__':
    app.run(debug=True)
