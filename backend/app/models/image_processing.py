from backend.app import db

class MedicalImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String(500), nullable=False)
    processed_image_path = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<MedicalImage {self.id}>'