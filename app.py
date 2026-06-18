from flask import Flask, request, jsonify
from routes.appointments import appointment_bp
from routes.chatbot import chatbot_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(appointment_bp, url_prefix="/api/appointments")
app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")

@app.route('/')
def home():
    return "DentSmiles Backend Running!"

if __name__ == '__main__':
    app.run(debug=True)
