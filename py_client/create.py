
import requests

headers = {'Authorization': 'Bearer 5e1703633976af2da40b1f525897888c265c73e6'}
endpoint = "http://127.0.0.1:8000/api/products/"

# http://127.0.0.1:8000
# session - > psot data

data={"title":"this field is filled",
      "price":34.66
}
get_response = requests.post(endpoint,json=data,headers=headers) # http get req 


print(get_response.json())

# if token is deleted by the admin it requires to log back in and thus creting a new token