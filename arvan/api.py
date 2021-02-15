import logging
import os
from urllib.parse import urlencode

import requests
from requests import Response


class Arvan:
	def __init__(self, api_key: str = None):
		if api_key:
			self.api_key = api_key
		else:
			self.api_key = os.environ.get('AR_API_KEY')

	def _build_headers(self):
		assert self.api_key, 'API KEY must be provided.'
		return {'AUTHORIZATION': self.api_key}

	def _render_response(self, response: Response):
		return response.json()

	def _send_request(self, method: str, url: str, data: dict = None, query_params: dict = None):
		if method.lower() == 'get':
			if query_params and len(query_params):
				url = url + '?%s' % (urlencode(query_params))
			r = requests.get(url, headers=self._build_headers())
			return self._render_response(r)

	def send_request(self, method: str, url: str, data: dict = None, query_params: dict = None):
		return self._send_request(method, url, data, query_params)
