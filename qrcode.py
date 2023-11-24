import pyotp
import qrcode

def generate_secret():
    # Generate a random base32-encoded secret
    return pyotp.random_base32()

def generate_qr_code(secret, username):
    # Generate a URL for QR code
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(name=username, issuer_name="YourApp")

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Display the QR code
    img.show()

def simulate_user_login(secret):
    # Simulate a user logging in
    totp = pyotp.TOTP(secret)

    # Simulate user entering OTP
    user_input = input("Enter the OTP code from your authenticator app: ")

    # Verify the user's input
    if totp.verify(user_input):
        print("Authentication successful!")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    # Step 1: Generate a random secret for the user
    user_secret = generate_secret()

    # Step 2: Generate and display the QR code
    generate_qr_code(user_secret, "testuser")

    # Step 3: Simulate the user logging in
    simulate_user_login(user_secret)
