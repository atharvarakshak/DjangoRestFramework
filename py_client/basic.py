# imp ********************
# HTTP request -> HTML
# Rest API req -> JSON
import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

# api -> 
get_response = requests.post(endpoint,json={"title":"abc123","content":None,"price":"22"}) # http get req 
# print(get_response.headers)
# print(get_response.text)


# Javascript object Notation is almost a Python dictionary not completly

print(get_response.json())
 #python dictionary

# print(get_response.status_code) #python dictionary
