from backend.app import db

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    treatment_plan = db.Column(db.String(500), nullable=False)
    medication = db.Column(db.String(200))
    warnings = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Recommendation {self.id}>'