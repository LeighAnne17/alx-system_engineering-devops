import json
import requests

def fetch_data():
    """Fetch the data from the API or any source."""
    url = 'https://jsonplaceholder.typicode.com/todos'  # Replace with your data source
    response = requests.get(url)
    return response.json()

def transform_data(data):
    """Transform the data into the required format."""
    tasks_by_user = {}
    for task in data:
        user_id = str(task['userId'])
        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []
        task_info = {
            "username": task['username'],
            "task": task['title'],
            "completed": task['completed']
        }
        tasks_by_user[user_id].append(task_info)
    return tasks_by_user

def save_to_json(data, filename):
    """Save the transformed data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    data = fetch_data()
    transformed_data = transform_data(data)
    save_to_json(transformed_data, 'todo_all_employees.json')

if __name__ == "__main__":
    main()
