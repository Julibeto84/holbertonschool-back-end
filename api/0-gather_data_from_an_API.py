#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                 .format(employee_id))
    todos_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                                  .format(employee_id))

    user = user_response.json()
    todos = todos_response.json()

    if not user or not todos:
        print("Error: No data found for the provided employee ID.")
        sys.exit(1)

    completed = [todo["title"] for todo in todos if todo.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
    user.get("name"), len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task))
