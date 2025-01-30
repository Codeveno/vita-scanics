from app import db

class ImageProcessing(db.Model):
    __tablename__ = 'image_processing'
    
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    processed_image = db.Column(db.String(255), nullable=True)
