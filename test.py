import unittest
from fastapi.testclient import TestClient
from main import app

class TestMemeAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_memes(self):
        response = self.client.get("/memes")
        self.assertEqual(response.status_code, 200)

    def test_get_meme(self):
        response = self.client.get("/memes/1")
        self.assertEqual(response.status_code, 200)

    def test_create_meme(self):
        meme = {"image": "image", "text": "text"}
        response = self.client.post("/memes", json=meme)
        self.assertEqual(response.status_code, 201)

    def test_update_meme(self):
        meme = {"image": "image", "text": "text"}
        response = self.client.put("/memes/1", json=meme)
        self.assertEqual(response.status_code, 200)

    def test_delete_meme(self):
        response = self.client.delete("/memes/1")
        self.assertEqual(response.status_code, 204)

if __name__ == "__main__":
    unittest.main()