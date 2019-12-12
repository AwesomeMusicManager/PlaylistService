import json
import unittest
from src.app import app

class PlaylistService(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.client.testing = True

    def test_creating_playlist(self):
        resp = self.client.get(path='/api/v1/create-playlist?withName=oi')
        self.assertEqual(resp.status_code, 200)

    def test_404(self):
        resp = self.client.get(path='/fake-url')
        self.assertEqual(resp.status_code, 404)

    def test_title_oi(self):
        resp = self.client.get(path='/api/v1/create-playlist?withName=oi')
        self.assertEqual(resp.json[0]['title'], 'Oi, Jesus')