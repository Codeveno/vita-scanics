from app import db

class PatientAnalysis(db.Model):
    __tablename__ = 'patient_analysis'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    analysis_result = db.Column(db.Text, nullable=True)
    
    patient = db.relationship('Patient', backref=db.backref('patient_analysis', lazy=True))
