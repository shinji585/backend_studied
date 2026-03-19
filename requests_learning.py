import requests
import json
# the first method to study is get, we know get is use to take information back to us 
api_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(api_url) # nos devuelve la url 

print(response.json())
print(response.status_code)
print(response.headers["Content-Type"])

# let's try to make a post 
todo = {
    "userId": 1, 
    "title": "Buy milk", 
    "completed": False
}
headers = {"Content-Type": "application/json"}
response = requests.post(api_url,data=json.dumps(todo),headers=headers)


print("\nResult: ",response.json())

# put 
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url + "/10",json=todo)
print(response.json())
print(response.status_code)

todo = {"title": "Mow lawn"}
response = requests.patch(api_url + "/10",json=todo)
print(f"\nRespuesta: {response.json()}")


# delete 

response = requests.delete(api_url + "/10")
print(response.json(), response.status_code)