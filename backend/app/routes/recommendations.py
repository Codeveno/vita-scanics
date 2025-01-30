from flask import Blueprint, request, jsonify
from app.models.recommendation_engine import RecommendationEngine
from app import db

bp = Blueprint('recommendations', __name__)

@bp.route('/recommendations', methods=['POST'])
def add_recommendation():
    data = request.get_json()
    new_recommendation = RecommendationEngine(**data)
    db.session.add(new_recommendation)
    db.session.commit()
    return jsonify({"message": "Recommendation added successfully", "recommendation": new_recommendation.id}), 201

@bp.route('/recommendations/<int:id>', methods=['GET'])
def get_recommendation(id):
    recommendation = RecommendationEngine.query.get(id)
    if recommendation:
        return jsonify({"recommendation": recommendation.recommendation})
    return jsonify({"message": "Recommendation not found"}), 404
