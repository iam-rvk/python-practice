import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
