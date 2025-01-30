from app import db

class DifferentialDiagnosis(db.Model):
    __tablename__ = 'differential_diagnosis'
    
    id = db.Column(db.Integer, primary_key=True)
    diagnosis = db.Column(db.String(100), nullable=False)
    potential_conditions = db.Column(db.Text, nullable=False)
