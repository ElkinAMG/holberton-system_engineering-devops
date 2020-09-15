#!/usr/bin/python3
"""This script returns information from an API.
"""
import json, requests, sys

employeer_id = sys.argv[1]

user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employeer_id)).json()
todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

tasks = [i for i in todos if i.get('userId') is user.get('id')]
titles = []
status = []
total = 0

for task in tasks:
    status.append(task.get('completed'))
    titles.append(task.get('title'))
    total += 1

employee = {"{}".format(user.get('id')): []}

for i in range(total):
    employee.get("{}".format(user.get('id'))).append({
    'task': titles[i],
    'completed': status[i],
    'username': user.get('username')
    })

with open('{}.json'.format(user.get('id')), 'w', newline='') as json_file:
    json.dump(employee, json_file, indent=4)
