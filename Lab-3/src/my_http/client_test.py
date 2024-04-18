import unittest
import json

import client


URL = 'https://httpbin.org/delay/4'
PROXY = {'https': 'http://117.250.3.58:8080'}


class ClientTest(unittest.TestCase):
	def test_get(self):
		response = []
		client.request('GET', URL, None, None, None, response)
		self.assertEqual(response[0], 200)

	def test_proxy(self):
		response_1 = []
		response_2 = []
		client.request('GET', URL, None, None, None, response_1)
		client.request('GET', URL, PROXY, None, None, response_2)
		orig_ip = json.loads(response_1[1]).get('origin')
		prox_ip = json.loads(response_2[1]).get('origin')
		self.assertNotEqual(orig_ip, prox_ip)
