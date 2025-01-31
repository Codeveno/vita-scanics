from flask import Blueprint, request, jsonify
from backend.app.models.emergency_alerts import EmergencyAlert
from backend.app import db

emergency_alerts_bp = Blueprint('emergency_alerts', __name__)

@emergency_alerts_bp.route('/trigger', methods=['POST'])
def trigger_alert():
    data = request.get_json()
    patient_id = data.get('patient_id')
    alert_message = data.get('alert_message')

    if patient_id and alert_message:
        alert = EmergencyAlert(patient_id=patient_id, alert_message=alert_message)
        db.session.add(alert)
        db.session.commit()
        return jsonify({'message': 'Emergency alert triggered', 'alert_id': alert.id}), 201

    return jsonify({'error': 'Invalid data'}), 400