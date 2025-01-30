import unittest
from app.models.image_processing import ImageProcessing
from app import app, db

class ImageProcessingTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_image_upload(self):
        response = self.app.post('/upload_image', data={'image': (open('test_image.jpg', 'rb'), 'test_image.jpg')})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Image uploaded successfully', response.get_data(as_text=True))
