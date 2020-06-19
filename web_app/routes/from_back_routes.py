import requests
import json

# Using requests
backend_url1 = f"https://api.openaq.org/v1/cities"
backend_url2 = f"https://api.openaq.org/v1/cities"
backend_url3 = f"https://api.openaq.org/v1/countries"
backend_url4 = f"https://api.openaq.org/v1/fetches"

backend_list=[backend_url1, backend_url2, backend_url3, backend_url4]

response1 = requests.get(backend_url1)
response2 = requests.get(backend_url2)
response3 = requests.get(backend_url3)
response4 = requests.get(backend_url4)

parsed_response1 = json.loads(response1.text)
parsed_response1 = json.loads(response2.text)
parsed_response1 = json.loads(response3.text)
parsed_response1 = json.loads(response4.text)