# Sentiment as a service

## Installation

### Docker
```sh
docker build -t sas .
docker run -d --name sas_instance_1 -p 8001:8001 sas
```

### Non-Docker
```
pip install -r requirements.txt
python app.py
```


## Usage
HTTP  
```
GET /sentiment/v1?query=food was not bad HTTP/1.1
```

cURL  
```curl
curl -X GET \
  'http://localhost:8080/sentiment/v1?query=food%20was%20not%20bad' \
  -H 'Postman-Token: 4baa6475-b922-4491-9ad8-10d15f534a39' \
  -H 'cache-control: no-cache'
```

PYTHON

```python
import requests

url = "http://localhost:8080/sentiment/v1"

querystring = {"query":"food%20was%20not%20bad"}

response = requests.request("GET", url, params=querystring)

print(response.text)
```
