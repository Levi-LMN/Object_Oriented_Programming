# app.py

from flask import Flask, render_template, jsonify, request
import pyotp
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

def generate_secret():
    return pyotp.random_base32()

def generate_qr_code(secret, username):
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(name=username, issuer_name="YourApp")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO object
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    # Encode the image data to base64
    img_base64 = base64.b64encode(img_byte_array.read()).decode('utf-8')
    return img_base64

def simulate_user_login(secret, user_input):
    totp = pyotp.TOTP(secret)
    return {"success": totp.verify(user_input)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-qr-code', methods=['GET'])
def generate_qr_code_route():
    user_secret = generate_secret()
    username = "testuser"
    qr_code_data = generate_qr_code(user_secret, username)

    return jsonify({"success": True, "qrCodeData": qr_code_data, "secret": user_secret})

@app.route('/simulate-login', methods=['GET'])
def simulate_login_route():
    user_secret = request.args.get('secret')
    user_input = request.args.get('otp')
    result = simulate_user_login(user_secret, user_input)
    return jsonify(result)

# New route for verifying the OTP
@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    user_input = request.form.get('otp')
    secret = request.form.get('secret')

    totp = pyotp.TOTP(secret)
    current_otp = totp.now()
    print(f"Current OTP: {current_otp}")

    print(f"Received OTP: {user_input}")
    print(f"Current OTP: {totp.now()}")  # Print the current OTP for comparison

    if totp.verify(user_input):
        return jsonify({"success": True, "message": "Authentication successful!"})
    else:
        return jsonify({"success": False, "message": "Authentication failed."})

if __name__ == '__main__':
    app.run(debug=True)







##html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OTP Generator</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrious/4.0.2/qrious.min.js"></script>
</head>
<body>

<h1>OTP Generator</h1>

<button onclick="generateQRCode()">Generate QR Code</button>

<div id="qr-code-container"></div>
<button onclick="verifyUserOTP()">Verify OTP</button>
<script>
    function generateQRCode() {
        // Use fetch API to call the Flask endpoint for generating QR code
        fetch('/generate-qr-code')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    // Display the QR code image on the page
                    console.log("QR code data received:", data.qrCodeData);

                    var qrCodeContainer = document.getElementById('qr-code-container');
                    qrCodeContainer.innerHTML = '';  // Clear previous content

                    // Create an image element and set its src to the QR code data
                    var qrCodeImage = new Image();
                    qrCodeImage.src = 'data:image/png;base64,' + data.qrCodeData;
                    qrCodeImage.style.width = '300px'; // Set the width as needed
                    qrCodeContainer.appendChild(qrCodeImage);

                    console.log("QR code container content:", qrCodeContainer.innerHTML);
                } else {
                    console.error("Error generating QR code:", data.error);
                    alert("Error generating QR code.");
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert("Error generating QR code.");
            });
    }


    // Assume 'secret' is available globally, replace with the actual value from the server
    var secret = ""; // Set the secret obtained from the server

    function simulateUserLogin() {
        var userInput = prompt("Enter the OTP code from your authenticator app:");
        var endpointURL = "/simulate-login?secret=" + secret + "&otp=" + userInput;

        // Use fetch API to call the Flask endpoint for simulating user login
        fetch(endpointURL)
            .then(response => response.json())
            .then(data => {
                alert(data.success ? "Authentication successful!" : "Authentication failed.");
            })
            .catch(error => {
                console.error('Error:', error);
                alert("Error verifying OTP.");
            });
    }

     function verifyUserOTP() {
    var userInput = prompt("Enter the OTP code from your authenticator app:");

    // You need to replace the following URL with the Flask endpoint for verifying OTP
    var endpointURL = "/verify-otp";

    // Use fetch API to call the Flask endpoint for verifying OTP
    fetch(endpointURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'otp': userInput,
            'secret': secret,  // Pass the secret generated for the user
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Verification result:", data);
        if (data.success) {
            alert("Authentication successful!");
        } else {
            alert("Authentication failed.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Error verifying OTP.");
    });
}



</script>

</body>
</html>
