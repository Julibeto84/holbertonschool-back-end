#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def fetch_todo_list_progress(employee_id):
    # API URL
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Make the request to the API
    response = requests.get(api_url)

    # Check the status code of the response
    if response.status_code != 200:
        print(f"Error: Unable to fetch data for employee {employee_id}")
        return
    
    # Convert a JSON string to a Python object
    todos = response.json()

    # Filter completed and uncompleted tasks
    completed_tasks = [list(filter(lambda todo: todo['completed'], todos))]
    total_tasks = len(todos)

    # Display the information in the required format
    print("Employee {} is done with tasks({}/{}):".
          format(todos, completed_tasks, total_tasks))
    
    for task in completed_tasks:
         print("\t {}".format(task))

if __name__ == "__main__":
    # Check if an argument (employee ID) is given
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command line arguments
    employee_id = int(sys.argv[1])

    # Call the function to obtain and print the information.
    fetch_todo_list_progress(employee_id)
