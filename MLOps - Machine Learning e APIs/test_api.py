import requests
import json
from http import HTTPStatus

auth = requests.auth.HTTPBasicAuth('lemsantos', '9Z1&2VZwK6wS')

response = requests.post('http://localhost:5000/quotation', json={
    'size': 120,
    'year': 2001,
    'garage': 2,
}, auth=auth)

assert response.status_code == HTTPStatus.OK

print(json.dumps(response.json(), indent=2))
