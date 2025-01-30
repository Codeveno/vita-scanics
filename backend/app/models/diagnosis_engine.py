from app import db

class DiagnosisEngine(db.Model):
    __tablename__ = 'diagnosis_engine'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    engine_output = db.Column(db.String(255), nullable=False)
    
    patient = db.relationship('Patient', backref=db.backref('diagnosis_engine', lazy=True))
