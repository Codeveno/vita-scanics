from flask import Blueprint, request, jsonify
from backend.app.models.image_processing import MedicalImage
from backend.app import db

image_upload_bp = Blueprint('image_upload', __name__)

@image_upload_bp.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    patient_id = request.form.get('patient_id')

    if file and patient_id:
        image = MedicalImage(patient_id=patient_id, image_path=file.filename)
        db.session.add(image)
        db.session.commit()
        return jsonify({'message': 'Image uploaded successfully', 'image_id': image.id}), 201

    return jsonify({'error': 'Invalid file or patient ID'}), 400