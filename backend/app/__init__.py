from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    db.init_app(app)

    # Register blueprints
    from .routes.image_upload import image_upload_bp
    from .routes.patient_data import patient_data_bp
    from .routes.diagnosis import diagnosis_bp
    from .routes.recommendations import recommendations_bp
    from .routes.telemedicine import telemedicine_bp
    from .routes.emergency_alerts import emergency_alerts_bp

    app.register_blueprint(image_upload_bp)
    app.register_blueprint(patient_data_bp)
    app.register_blueprint(diagnosis_bp)
    app.register_blueprint(recommendations_bp)
    app.register_blueprint(telemedicine_bp)
    app.register_blueprint(emergency_alerts_bp)

    return app