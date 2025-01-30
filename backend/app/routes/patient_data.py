from flask import Blueprint, request, jsonify
from app.models.patient import Patient
from app import db

bp = Blueprint('patient_data', __name__)

@bp.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(**data)
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added successfully", "patient": new_patient.id}), 201

@bp.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get(id)
    if patient:
        return jsonify({"first_name": patient.first_name, "last_name": patient.last_name})
    return jsonify({"message": "Patient not found"}), 404
