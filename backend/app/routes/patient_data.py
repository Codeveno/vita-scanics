from flask import Blueprint, request, jsonify
from backend.app.models.patient_analysis import PatientAnalysis
from backend.app import db

patient_data_bp = Blueprint('patient_data', __name__)

@patient_data_bp.route('/add', methods=['POST'])
def add_patient_data():
    data = request.get_json()
    patient_id = data.get('patient_id')
    symptoms = data.get('symptoms')
    medical_history = data.get('medical_history')
    lab_results = data.get('lab_results')

    if patient_id and symptoms:
        patient_data = PatientAnalysis(
            patient_id=patient_id,
            symptoms=symptoms,
            medical_history=medical_history,
            lab_results=lab_results
        )
        db.session.add(patient_data)
        db.session.commit()
        return jsonify({'message': 'Patient data added successfully', 'data_id': patient_data.id}), 201

    return jsonify({'error': 'Invalid data'}), 400