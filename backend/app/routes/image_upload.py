from flask import Blueprint, request, jsonify
from app.models.image_processing import ImageProcessing
from app import db

bp = Blueprint('image_upload', __name__)

@bp.route('/upload_image', methods=['POST'])
def upload_image():
    image = request.files.get('image')
    if image:
        image_url = "path/to/save/image"
        new_image = ImageProcessing(image_url=image_url)
        db.session.add(new_image)
        db.session.commit()
        return jsonify({"message": "Image uploaded successfully", "image_url": image_url}), 201
    return jsonify({"message": "No image provided"}), 400
