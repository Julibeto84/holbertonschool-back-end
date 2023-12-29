#!/usr/bin/python3
'''For a given employee ID, returns information about his/her TODO list progress.'''

if __name__ == '__main__':
    import requests
    from sys import argv

    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')

    # Comprobamos que la respuesta de la API sea exitosa
    if user_response.status_code != 200:
        print("Error: Unable to retrieve data from the API.")
        exit(1)

    user = user_response.json()

    # Comprobamos que tenemos datos válidos
    if not user:
        print("Error: No data found for the provided employee ID.")
        exit(1)

    # Truncar el nombre y agregar puntos suspensivos si es necesario
    max_name_length = 18
    truncated_name = (user['name'][:max_name_length - 3] + '...') if len(user['name']) > max_name_length else user['name']

    # Imprimir solo el nombre del usuario
    print(f"Employee Name: {truncated_name}")

