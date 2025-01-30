from app import db

class ClinicalTrials(db.Model):
    __tablename__ = 'clinical_trials'
    
    id = db.Column(db.Integer, primary_key=True)
    trial_name = db.Column(db.String(100), nullable=False)
    trial_description = db.Column(db.Text, nullable=True)
    eligibility_criteria = db.Column(db.Text, nullable=True)
