#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Get employee information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get employee TODO list
    todos_response = requests.get(f'{base_url}/todos', params={'userId': employee_id})
    todos_data = todos_response.json()

    # Calculate number of completed tasks and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    # Print the progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
