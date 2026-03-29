import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # VULNERABILITY: This allows DAST to find potential issues
    user_input = request.args.get('name', 'Guest')
    return f"<h1>Hello {user_input}</h1><p>SPD Test Server is Running!</p>"

@app.route('/danger')
def danger():
    # SAST VULNERABILITY: Bandit will flag this 'os.system'
    cmd = request.args.get('cmd')
    os.system(cmd) 
    return "Executed"

if __name__ == "__main__":
    # Port 5000 matches our SPD Onboarding default
    app.run(host='0.0.0.0', port=5000)