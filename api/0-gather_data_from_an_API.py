#!/usr/bin/python3
""" Getting my first apis """

from json import loads
from requests import get
import sys


def get_employee_todo_progress(employee_id):

    # Fetch TODO list from the API
    todos_response = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(employee_id))
    todos = loads(todos_response.text)

    # Fetch user name from the API
    users_response = get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(employee_id))
    user = loads(users_response.text)

    # Filter completed tasks
    todos_done = list(filter(lambda todo: todo['completed'], todos))

    # Count completed and total tasks
    number_of_done_tasks = len(todos_done)
    total_number_of_tasks = len(todos)

   # Display the progress
    employee_name = user.get('name', 'Unknown')
    print("Employee {} is done with tasks ({}/{})"
          .format(employee_name, number_of_done_tasks, total_number_of_tasks))


    # Display completed tasks
    for todo in todos_done:
        print(f"\t {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
