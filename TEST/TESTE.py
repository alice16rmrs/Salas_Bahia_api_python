import unittest
import json
import requests


class TestAPI(unittest.TestCase):

    def test_delete_3(self):
        req = requests.delete('http://localhost:5000/crud/api/produtos/1')
        self.assertTrue(req.ok)

    def test_delete_4(self):
        req = requests.delete('http://localhost:5000/crud/api/produtos/4')
        self.assertTrue(req.ok)

    def test_get_3(self):
        req = requests.get('http://localhost:5000/crud/api/produtos/1')
        self.assertTrue(req.ok)

    def test_get_4(self):
        req = requests.get('http://localhost:5000/crud/api/produtos/4')
        self.assertTrue(req.ok)

    def test_post_4(self):
        data = {
            'nome': "Microondas",
            'qtd': 10
        }

        headers = {
            'Content-Type': 'application/json',
        }

        req = requests.post('http://localhost:5000/crud/api/produtos', headers=headers, data=json.dumps(data))
        self.assertTrue(req.ok)

    def test_post_5(self):
        data = {
            'nome': "Computador",
            'qtd': "Não-definido"
        }

        headers = {
            'Content-Type': 'application/json',
        }

        req = requests.post('http://localhost:5000/crud/api/produtos', headers=headers, data=json.dumps(data))
        self.assertTrue(req.ok)

    def test_put_3(self):
        data = {
            'nome': "Microondas",
            'qtd': 40
        }

        headers = {
            'Content-Type': 'application/json',
        }

        req = requests.put('http://localhost:5000/crud/api/produtos/1', headers=headers, data=json.dumps(data))
        self.assertTrue(req.ok)

    def test_put_4(self):
        data = {
            'nome': "Microondas",
            'qtd': 49
        }

        headers = {
            'Content-Type': 'application/json',
        }

        req = requests.put('http://localhost:5000/crud/api/produtos/4', headers=headers, data=json.dumps(data))
        self.assertTrue(req.ok)


if __name__ == '__main__':
    unittest.main()
