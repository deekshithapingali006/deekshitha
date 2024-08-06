from flask import Flask, render_template, request
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64

app = Flask(__name__)

SECRET_KEY = b'Sixteen byte key'  # 16-byte key for DES3

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt(text):
    text = pad(text)
    cipher = DES3.new(SECRET_KEY, DES3.MODE_ECB)
    encrypted_text = cipher.encrypt(text.encode('utf-8'))
    encoded_text = base64.b64encode(encrypted_text).decode('utf-8')
    return encoded_text

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_amount = None
    if request.method == 'POST':
        amount = request.form['amount']
        encrypted_amount = encrypt(amount)
    return render_template('index.html', encrypted_amount=encrypted_amount)

if __name__ == '__main__':
    app.run(debug=True)
