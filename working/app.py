# app.py
from flask import Flask, render_template, jsonify, request, redirect, url_for, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import random
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = '20405041018'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'retailsysx@gmail.com'
app.config['MAIL_PASSWORD'] = 'qecs yhcc gkeq nlee'
app.config['MAIL_DEFAULT_SENDER'] = 'retailsysx@gmail.com'

mail = Mail(app)
otp_storage = {}  # Temporary storage for demonstration purposes

login_manager = LoginManager(app)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'levi'
app.config['MYSQL_PASSWORD'] = 'levi'
app.config['MYSQL_DB'] = 'retailsysx'
mysql = MySQL(app)


# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cart_items = db.relationship('CartItem', backref='user', lazy=True)

# Define the CartItem model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_name = db.Column(db.String(80), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Email('{self.address}')"



# Create the tables within the application context
with app.app_context():
    db.create_all()

def generate_otp():
    # Generate a random 6-digit number
    return '{:06}'.format(random.randint(0, 999999))

def send_otp_email(email, otp):
    msg = Message('Your OTP', recipients=[email])
    msg.body = f'Your OTP is: {otp}'
    mail.send(msg)

@app.route('/')
def index():
    return render_template('index.html')

##USER LOGIN PAGE
@app.route('/user/user_login_page')
def user_login_page():
    return render_template('user/login.html')

#ADMIN LOGIN PAGE
@app.route('/admin/admin_login_page')
def admin_login_page():
    return render_template('admin/login.html')

##ADMIN PANEL
# Add this line to your 'send_otp' route
@app.route('/send-otp', methods=['POST'])
def send_otp():
    email = request.form.get('email')

    # Check if the email exists in the Email model
    existing_email = Email.query.filter_by(email=email).first()
    if not existing_email:
        abort(400, "Email does not exist. Please register first.")

    otp = generate_otp()
    otp_storage[email] = otp  # Store OTP temporarily for verification

    print(f'Generated OTP for {email}: {otp}')

    send_otp_email(email, otp)
    return jsonify({"success": True, "message": "OTP sent successfully! Please check your email."})


@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    email_address = request.form.get('email')
    user_input = request.form.get('otp')

    stored_otp = otp_storage.get(email_address)

    if stored_otp and stored_otp == user_input:
        del otp_storage[email_address]
        return jsonify({"success": True, "message": "Authentication successful!"}), 302
    else:
        return jsonify({"success": False, "message": "Authentication failed."})


@app.route('/admin_page')
def admin_page():
    emails = Email.query.all()  # Fetch all email addresses from the database
    return render_template('admin/index.html', emails=emails)

@app.route('/main')
def main():
    if 'email' in session:
        email = session['email']
        return render_template('admin/index.html', email=email)
    else:
        return redirect(url_for('admin_page'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Add a route for serving other static files (images, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)


@app.route('/login_page')
def login_page():
    return render_template('login_main.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username'].strip()
    password = request.form['password'].strip()

    user = User.query.filter_by(username=username).first()
    print(f'Entered Username: {username}, Entered Password: {password}, User from DB: {user}')

    if user and check_password_hash(user.password, password):
        # Redirect to the main page after successful login_main
        return redirect(url_for('user_main'))



    return render_template('user/templates/login_alert.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    new_username = request.form['new_username']
    new_password = request.form['new_password']

    if not new_username or not new_password:
        return 'Username and password are required.'

    hashed_password = generate_password_hash(new_password)

    new_user = User(username=new_username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"status": "success", "message": f'User {new_username} added successfully! \n you may now Login'})
    except:
        db.session.rollback()
        return jsonify({"status": "error", "message": f'Username {new_username} already exists. Please choose a different username.'})



# Define the get_products function
def get_products():
    # Fetch products from the database
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, price FROM products")  # Assuming your table has columns 'name' and 'price'
    products = cur.fetchall()
    cur.close()
    return products

# Route for the products page
@app.route('/products')
def products():
    # Get products data
    products_data = get_products()

    # Pass the product data to the template
    return render_template('products.html', products=products_data)

# Route for the index page (main route)
@app.route('/user_main')
def user_main():
    # Get products data
    products_data = get_products()

    # Pass the product data to the template
    return render_template('user/templates/index.html', products=products_data)





@app.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    try:
        data = request.get_json()
        product_name = data.get('name')
        product_price = data.get('price')
        quantity = data.get('quantity', 1)

        # Check if the item is already in the cart, and update the quantity if it is
        existing_item = CartItem.query.filter_by(user_id=current_user.id, product_name=product_name).first()

        if existing_item:
            existing_item.quantity += quantity
        else:
            # Create a new cart item
            cart_item = CartItem(
                user_id=current_user.id,
                product_name=product_name,
                product_price=product_price,
                quantity=quantity
            )

            db.session.add(cart_item)

        db.session.commit()

        return jsonify(success=True)

    except Exception as e:
        db.session.rollback()
        print(f"Error adding item to cart: {str(e)}")
        return jsonify(success=False, error=str(e))


@app.route('/get_cart_items', methods=['GET'])
@login_required
def get_cart_items():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    cart_data = [
        {
            'product_name': item.product_name,
            'product_price': item.product_price,
            'quantity': item.quantity
        }
        for item in cart_items
    ]
    return jsonify(cart_data)


# Route to view all email addresses
@app.route('/view-emails')
def view_emails():
    emails = Email.query.all()
    return render_template('admin/view_emails.html', emails=emails)

# Route to add an email address
@app.route('/add-email', methods=['POST'])
def add_email():
    email_address = request.form.get('email')

    # Check if the email already exists
    existing_email = Email.query.filter_by(email=email_address).first()

    if existing_email:
        return jsonify({'success': False, 'message': 'Email already exists.'})
    else:
        new_email = Email(email=email_address)
        db.session.add(new_email)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Email added successfully.'})

# Route to delete an email address
@app.route('/delete-email/<int:email_id>', methods=['POST'])
def delete_email(email_id):
    email = Email.query.get_or_404(email_id)
    db.session.delete(email)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Email deleted successfully.'})


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form['email']

        # Perform any necessary validation on the email address

        # Send email
        to_email = email  # Use the entered email address as the recipient
        subject = 'New Subscriber'

        # Make the message longer
        message = f'Thank you for subscribing to our newsletter!\n\n'
        message += f'We appreciate your interest and look forward to keeping you updated on our latest news and events.\n\n'
        message += f'Best regards,\nThe RetailsysX Team\n\n'
        message += f'---\nOriginal Email: {email}'
        message += f'\nUnsubscribe: https://www.retailsysx.com/unsubscribe'



        # Replace with your SMTP server details
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'retailsysx@gmail.com'
        smtp_password = 'qecs yhcc gkeq nlee'  # Use the generated app password

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)

            server.sendmail(smtp_username, to_email, f'Subject: {subject}\n\n{message}')

        return 'Subscription successful'


if __name__ == '__main__':
    app.run(debug=True)
