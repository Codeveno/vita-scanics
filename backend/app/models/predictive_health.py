from backend.app import db

class PredictiveHealth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    predicted_condition = db.Column(db.String(200), nullable=False)
    risk_score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<PredictiveHealth {self.id}>'