import requests

print(requests.get('http://192.168.0.94:5000/table').json())
