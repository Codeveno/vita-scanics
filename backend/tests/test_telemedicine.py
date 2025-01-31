import unittest
from backend.app import create_app, db
from backend.app.models.telemedicine import TelemedicineSession

class TestTelemedicine(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_start_session(self):
        response = self.client.post('/telemedicine/start', json={
            'patient_id': 1,
            'doctor_id': 1
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()