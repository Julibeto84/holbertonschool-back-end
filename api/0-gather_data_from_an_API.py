#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
        tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                         format(argv[1]))

        completed = [t.get("title") for t in todos if t.get("completed") is True]
        print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
        [print("\t {}".format(c)) for c in completed]
