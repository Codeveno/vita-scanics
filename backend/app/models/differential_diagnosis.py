from backend.app import db

class DifferentialDiagnosis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    possible_conditions = db.Column(db.String(500), nullable=False)
    risk_factors = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<DifferentialDiagnosis {self.id}>'