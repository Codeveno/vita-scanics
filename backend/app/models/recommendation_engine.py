from app import db

class RecommendationEngine(db.Model):
    __tablename__ = 'recommendation_engine'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    recommendation = db.Column(db.Text, nullable=False)
    
    patient = db.relationship('Patient', backref=db.backref('recommendation_engine', lazy=True))
