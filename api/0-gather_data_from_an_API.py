#!/usr/bin/python3

import sys
from requests import get
from json import loads

def get_employee_todo_progress(employee_id):
    # Fetch TODO list from the API
    response = get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos = loads(response.text)

    # Filter completed tasks
    todos_done = list(filter(lambda todo: todo['completed'], todos))

    # Count completed and total tasks
    number_of_done_tasks = len(todos_done)
    total_number_of_tasks = len(todos)

    # Fetch user name
    users_response = get('https://jsonplaceholder.typicode.com/users').json()
    employee_name = None
    for user in users_response:
        if user['id'] == employee_id:
            employee_name = user['name']
            break

    # Display the progress
    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")

    # Display completed tasks
    for todo in todos_done:
        print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
