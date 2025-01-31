from flask import Blueprint, request, jsonify
from backend.app.models.telemedicine import TelemedicineSession
from backend.app import db

telemedicine_bp = Blueprint('telemedicine', __name__)

@telemedicine_bp.route('/start', methods=['POST'])
def start_session():
    data = request.get_json()
    patient_id = data.get('patient_id')
    doctor_id = data.get('doctor_id')

    if patient_id and doctor_id:
        session = TelemedicineSession(patient_id=patient_id, doctor_id=doctor_id)
        db.session.add(session)
        db.session.commit()
        return jsonify({'message': 'Telemedicine session started', 'session_id': session.id}), 201

    return jsonify({'error': 'Invalid data'}), 400