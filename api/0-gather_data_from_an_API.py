#!/usr/bin/python3
'''For a given employee ID, returns information
   about his/her TODO list progress.'''

if __name__ == '__main__':
    import requests
    from sys import argv

    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    tasks_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    # Verificar si las respuestas de la API son exitosas
    if user_response.status_code != 200 or tasks_response.status_code != 200:
        print("Error: Unable to retrieve data from the API.")
        exit(1)

    user = user_response.json()
    tasks = tasks_response.json()

    # Verificar si se obtuvieron datos válidos
    if not user or not tasks:
        print("Error: No data found for the provided employee ID.")
        exit(1)

    done_list = []
    done_tasks = 0
    total_tasks = 0

    employee_name = user['name']
    for task in tasks:
        total_tasks += 1
        if task['completed']:
            done_list.append(task['title'])
            done_tasks += 1

    # Truncar el nombre y agregar puntos suspensivos si es necesario
    max_name_length = 18
    truncated_name = (employee_name[:max_name_length - 3] + '...') if len(employee_name) > max_name_length else employee_name

    print("Employee {} is done with tasks({}/{}):".format(truncated_name, done_tasks, total_tasks))
    for task in done_list:
        print("\t {}".format(task))

