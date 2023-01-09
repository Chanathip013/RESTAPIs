import requests
api_url =  'https://jsonplaceholder.typicode.com/todos/1'

todo = {
    "UserId" : 1,
    "id" : 909,
    "title" : 'Chanathip Boonma',
    "completed" : True
}

response = requests.get(api_url, json=todo)

print(response.json())
print(response.status_code)