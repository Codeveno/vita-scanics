from flask import Blueprint, request, jsonify
from app.models.diagnosis_engine import DiagnosisEngine
from app import db

bp = Blueprint('diagnosis', __name__)

@bp.route('/diagnosis', methods=['POST'])
def add_diagnosis():
    data = request.get_json()
    new_diagnosis = DiagnosisEngine(**data)
    db.session.add(new_diagnosis)
    db.session.commit()
    return jsonify({"message": "Diagnosis added successfully", "diagnosis": new_diagnosis.id}), 201

@bp.route('/diagnosis/<int:id>', methods=['GET'])
def get_diagnosis(id):
    diagnosis = DiagnosisEngine.query.get(id)
    if diagnosis:
        return jsonify({"diagnosis": diagnosis.diagnosis})
    return jsonify({"message": "Diagnosis not found"}), 404
