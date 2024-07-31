#!/usr/bin/python3
import requests
import sys
import json

def export_to_json(employee_id):
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Get employee information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    username = user_data.get('username')

    # Get employee TODO list
    todos_response = requests.get(f'{base_url}/todos', params={'userId': employee_id})
    todos_data = todos_response.json()

    # Prepare data for JSON export
    tasks = []
    for task in todos_data:
        task_info = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks.append(task_info)
    
    # Define the filename
    filename = f"{employee_id}.json"

    # Write data to JSON file
    with open(filename, 'w') as file:
        json.dump({str(employee_id): tasks}, file, indent=4)

    print(f"Data exported to {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)

