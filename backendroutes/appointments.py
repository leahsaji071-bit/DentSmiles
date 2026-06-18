from flask import Blueprint, request, jsonify

appointment_bp = Blueprint('appointments', __name__)

# For now just log data — no DB yet
@appointment_bp.route('/submit', methods=['POST'])
def submit_appointment():
    data = request.get_json()
    print("Received appointment:", data)

    return jsonify({"message": "Appointment received!"}), 200
