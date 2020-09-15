#!/usr/bin/python3
"""This script returns information from an API.
"""
import requests
import sys

employeer_id = sys.argv[1]

user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
    employeer_id)).json()
todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

tasks = [i for i in todos if i.get('userId') is user.get('id')]
completed = 0
total = 0

for task in tasks:
    total += 1
    if task.get('completed'):
        completed += 1

print('Employee {} is done with tasks({}/{}):'.format(
    user.get('name'), completed, total))

for task in tasks:
    if task.get('completed'):
        print('\t {}'.format(task.get('title')))
