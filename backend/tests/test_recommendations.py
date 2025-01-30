from backend.app.models.recommendation_engine import RecommendationEngine

def test_generate_recommendations():
    engine = RecommendationEngine()
    recommendations = engine.generate_recommendations("Condition Detected")
    assert len(recommendations) > 0
