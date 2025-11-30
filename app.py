from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import openai
import smtplib
from email.message import EmailMessage

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

OPENAI_KEY = os.environ.get('OPENAI_API_KEY')
EMAIL_USER = os.environ.get('EMAIL_USER')  # SMTP username (your email)
EMAIL_PASS = os.environ.get('EMAIL_PASS')  # SMTP app password
EMAIL_TO = os.environ.get('EMAIL_TO')      # Recipient (your email) for contact form

if OPENAI_KEY:
    openai.api_key = OPENAI_KEY

@app.route('/generate', methods=['POST'])
def generate():
    if not OPENAI_KEY:
        return jsonify({'error': 'OpenAI API key not configured on server.'})
    data = request.get_json() or {}
    user_text = data.get('text', 'Hello')
    try:
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': user_text}],
            max_tokens=300,
        )
        ai_text = resp['choices'][0]['message']['content']
        return jsonify({'response': ai_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    if not (name and email and message):
        return jsonify({'success': False, 'error': 'Missing fields'})

    if not (EMAIL_USER and EMAIL_PASS and EMAIL_TO):
        return jsonify({'success': False, 'error': 'Email not configured. Set EMAIL_USER, EMAIL_PASS, EMAIL_TO in environment.'})

    try:
        msg = EmailMessage()
        msg['Subject'] = f'Contact form message from {name} via Engineer_Abuibraheem site'
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_TO
        body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        msg.set_content(body)

        # Using SMTP to send email (works with Gmail when using app password)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Serve static files (index.html, etc.)
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
