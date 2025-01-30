from app import db

class PredictiveHealth(db.Model):
    __tablename__ = 'predictive_health'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    health_risk = db.Column(db.String(100), nullable=False)
    
    patient = db.relationship('Patient', backref=db.backref('predictive_health', lazy=True))
