#!/usr/bin/python3
'''For a given employee ID, returns information about his/her TODO list progress.'''

if __name__ == '__main__':
    import requests
    from sys import argv

    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos')

    # Comprobamos que la respuesta de la API sea exitosa
    if user_response.status_code != 200 or tasks_response.status_code != 200:
        print("Error: Unable to retrieve data from the API.")
        exit(1)

    user = user_response.json()
    tasks = tasks_response.json()

    # Comprobamos que tenemos datos válidos
    if not user or not tasks:
        print("Error: No data found for the provided employee ID.")
        exit(1)

    done_tasks = sum(1 for task in tasks if task['completed'])

    print(f"Employee {user['name']} is done with tasks({done_tasks}/{len(tasks)}):")
    for task in tasks:
        if task['completed']:
            print(f"\t {task['title']}")
