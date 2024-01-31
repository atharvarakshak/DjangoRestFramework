
import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data={"title":"this field is filled",
      "price":34.66}
get_response = requests.post(endpoint,json=data) # http get req 


print(get_response.json())

