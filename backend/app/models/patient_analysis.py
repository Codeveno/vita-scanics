from backend.app import db

class PatientAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    symptoms = db.Column(db.String(500), nullable=False)
    medical_history = db.Column(db.String(1000))
    lab_results = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<PatientAnalysis {self.id}>'