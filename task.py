import json
from collections import defaultdict

with open('source_file_2.json') as f:
    projects_list = json.load(f)

projects_list = sorted(projects_list, key=lambda project: project['priority']) 

watchers_dict = defaultdict(list)
managers_dict = defaultdict(list)

for project in projects_list:
    for watcher in project['watchers']:
        watchers_dict[watcher].append(project['name'])
    for manager in project['managers']:
        managers_dict[manager].append(project['name'])

with open('managers.json', 'w') as managers_outfile:
    json.dump(managers_dict, managers_outfile, indent=4)

with open('watchers.json', 'w') as watchers_outfile:
    json.dump(watchers_dict, watchers_outfile, indent=4)
