#!/usr/bin/python3
"""This script returns information from an API.
"""
import csv
import requests
import sys

employeer_id = sys.argv[1]

user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
    employeer_id)).json()
todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

tasks = [i for i in todos if i.get('userId') is user.get('id')]
titles = []
com = 0

for task in tasks:
    if task.get('completed'):
        com += 1
        titles.append(task.get('title'))

with open('{}.csv'.format(user.get('id')), 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for i in range(com):
        writer.writerow([user.get('id'), user.get('username'), com, titles[i]])
