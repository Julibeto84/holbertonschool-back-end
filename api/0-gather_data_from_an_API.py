#!/usr/bin/python3


from requests import get
from json import loads


# the required first parameter of the 'get' method is the 'url':
response = get('https://jsonplaceholder.typicode.com/todos')

todos = loads(response.text)
todos_done = list(filter(lambda todo: todo['completed'], todos))
users_tasks = dict()

for todo in todos:
    user_id = todo['userId']
    if user_id not in users_tasks:
        users_tasks[user_id] = list()
    user_title = todo['title']
    users_tasks[user_id].append(user_title)

# print the response text (the content of the requested file):
print(users_tasks)
