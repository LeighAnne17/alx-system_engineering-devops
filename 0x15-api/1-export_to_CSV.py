#!/usr/bin/python3
import requests
import sys
import csv

def export_to_csv(employee_id):
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Get employee information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    username = user_data.get('username')

    # Get employee TODO list
    todos_response = requests.get(f'{base_url}/todos', params={'userId': employee_id})
    todos_data = todos_response.json()

    # Define the filename
    filename = f"{employee_id}.csv"

    # Open the CSV file for writing
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Write each row to the CSV
        for task in todos_data:
            user_id = task.get('userId')
            task_title = task.get('title')
            task_completed = task.get('completed')
            writer.writerow([user_id, username, task_completed, task_title])

    print(f"Data exported to {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
