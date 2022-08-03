from run import app
import unittest

class FlaskTest(unittest.TestCase):
    
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'OK!' in response.data)


if __name__ == "__main__":
    unittest.main()