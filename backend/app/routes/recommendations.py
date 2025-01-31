from flask import Blueprint, request, jsonify
from backend.app.models.recommendation_engine import Recommendation
from backend.app import db

recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/add', methods=['POST'])
def add_recommendation():
    data = request.get_json()
    patient_id = data.get('patient_id')
    treatment_plan = data.get('treatment_plan')
    medication = data.get('medication')
    warnings = data.get('warnings')

    if patient_id and treatment_plan:
        recommendation = Recommendation(
            patient_id=patient_id,
            treatment_plan=treatment_plan,
            medication=medication,
            warnings=warnings
        )
        db.session.add(recommendation)
        db.session.commit()
        return jsonify({'message': 'Recommendation added successfully', 'recommendation_id': recommendation.id}), 201

    return jsonify({'error': 'Invalid data'}), 400