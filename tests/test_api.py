import json
import unittest
from src.app import app

class PlaylistService(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.client.testing = True

    def test_posting_a_blog(self):
        resp = self.client.get(path='/')
        self.assertEqual(resp.status_code, 200)