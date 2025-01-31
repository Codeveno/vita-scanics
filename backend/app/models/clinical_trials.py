from backend.app import db

class ClinicalTrial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    trial_name = db.Column(db.String(200), nullable=False)
    eligibility = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<ClinicalTrial {self.id}>'