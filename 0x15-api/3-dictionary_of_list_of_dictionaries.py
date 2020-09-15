#!/usr/bin/python3
""" Returns all employes"""
import json
import requests


if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    data = {}

    for user in users:
        tasks = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                tasks.append(taskDict)
        data[user.get('id')] = tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(data, f)
