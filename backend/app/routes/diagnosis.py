from flask import Blueprint, request, jsonify
from backend.app.models.diagnosis_engine import Diagnosis
from backend.app import db

diagnosis_bp = Blueprint('diagnosis', __name__)

@diagnosis_bp.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    patient_id = data.get('patient_id')
    condition = data.get('condition')
    confidence_level = data.get('confidence_level')

    if patient_id and condition and confidence_level:
        diagnosis = Diagnosis(patient_id=patient_id, condition=condition, confidence_level=confidence_level)
        db.session.add(diagnosis)
        db.session.commit()
        return jsonify({'message': 'Diagnosis recorded successfully', 'diagnosis_id': diagnosis.id}), 201

    return jsonify({'error': 'Invalid data'}), 400