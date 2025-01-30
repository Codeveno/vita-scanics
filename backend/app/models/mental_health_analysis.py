from app import db

class MentalHealthAnalysis(db.Model):
    __tablename__ = 'mental_health_analysis'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    mental_health_condition = db.Column(db.String(100), nullable=False)
    
    patient = db.relationship('Patient', backref=db.backref('mental_health_analysis', lazy=True))
