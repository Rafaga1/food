import unittest
import requests


class TestResponseMethods(unittest.TestCase):

    def test_good(self):
        import json

        data = {
            "is_vegan": 'true',
            "is_special": 'true',
            "topping": [
                "майоне",
                "перец"
            ]
        }
        request = requests.post('http://127.0.0.1:8000/dish', data=json.dumps(data))
        print(request)
        self.assertEqual(request.status_code, 200)

    def test_validation(self):
        import json

        data = {
            "is_vegan": 'truee',
            "is_special": 'true',
            "topping": [
                "майоне",
                "перец"
            ]
        }
        request = requests.post('http://127.0.0.1:8000/dish', data=json.dumps(data))
        print(request)
        self.assertEqual(request.status_code, 422)


if __name__ == '__main__':
    unittest.main()
