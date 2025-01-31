from backend.app import db

class MentalHealthAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    behavioral_patterns = db.Column(db.String(500), nullable=False)
    mental_condition = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<MentalHealthAnalysis {self.id}>'