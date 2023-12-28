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

    # Obtener la respuesta de la API para el usuario
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    # Obtener la respuesta de la API para los todos
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    # Convertir la respuesta a JSON
    user = user_response.json()
    todos = todos_response.json()

    # Verificar si se obtuvieron datos válidos
    if not user or not todos:
        print("Error: No data found for the provided employee ID.")
        sys.exit(1)

    # Depuración: imprimir la respuesta de la API directamente
    print("User API Response:", user_response.text)
    print("Todos API Response:", todos_response.text)

    # Filtrar tareas completadas
    completed = [todo["title"] for todo in todos if todo.get("completed")]

    # Extraer y depurar el nombre del empleado
    employee_name = user.get("name").strip()
    print("Employee Name:", employee_name)  # Depuración

    # Imprimir el progreso del empleado
    print(f"Employee {employee_name} is done with tasks({len(completed)}/{len(todos)}):")

    # Imprimir tareas completadas
    for task in completed:
        print(f"\t {task}")

