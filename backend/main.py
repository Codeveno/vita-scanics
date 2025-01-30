from flask import Flask
from app.models import db
from app.routes import image_upload, patient_data, diagnosis, recommendations, telemedicine, emergency_alerts

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize the database with app
db.init_app(app)

app.register_blueprint(image_upload.bp)
app.register_blueprint(patient_data.bp)
app.register_blueprint(diagnosis.bp)
app.register_blueprint(recommendations.bp)
app.register_blueprint(telemedicine.bp)
app.register_blueprint(emergency_alerts.bp)

if __name__ == '__main__':
    app.run(debug=True)
