#!/usr/bin/python3
"""
This module uses a REST API to return information about an employee's TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    employee_name = user.get("name")
    completed_tasks = [task for task in todos if task.get("userId") == int(employee_id) and task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title"))))
