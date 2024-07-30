#!/usr/bin/python3
'''
Gather employee TODO list progress from the API.
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

def fetch_employee_data(employee_id):
    """Fetch employee data and TODO tasks from the API."""
    try:
        # Fetch employee information
        response = requests.get(f'{REST_API}/users/{employee_id}')
        response.raise_for_status()  # Raise an exception for HTTP errors
        employee = response.json()
        employee_name = employee.get('name')
        
        # Fetch TODO tasks
        response = requests.get(f'{REST_API}/todos')
        response.raise_for_status()
        tasks = response.json()
        
        return employee_name, tasks
    
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)

    employee_name, tasks = fetch_employee_data(employee_id)
    
    # Filter tasks for the given employee ID
    tasks_for_employee = [task for task in tasks if task.get('userId') == employee_id]
    completed_tasks = [task for task in tasks_for_employee if task.get('completed')]
    
    # Display results
    print(f'Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(tasks_for_employee)}):')
    for task in completed_tasks:
        print(f'\t {task.get("title")}')

if __name__ == '__main__':
    main()
  
