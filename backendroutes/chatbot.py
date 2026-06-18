from flask import Blueprint, request, jsonify
import random

chatbot_bp = Blueprint('chatbot', __name__)

# Dummy dental tips
dental_tips = [
    "Tooth pain may indicate cavities or infection.",
    "Brush twice daily and floss to avoid gum disease.",
    "Visit a dentist every 6 months for a check-up.",
    "Avoid very cold or hot drinks if you have sensitivity."
]

@chatbot_bp.route('/ask', methods=['POST'])
def ask_bot():
    user_message = request.get_json().get("message")
    reply = random.choice(dental_tips)
    return jsonify({"reply": reply})
