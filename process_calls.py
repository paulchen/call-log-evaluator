#!/usr/bin/python

import sys, xmltodict, pprint
from datetime import datetime

calls = {}

for file in sys.argv[1:]:
    with open(file, 'r') as input_file:
        xml = input_file.read()
        data = xmltodict.parse(xml)
        for call in data['calls']['call']:
            key = call['@number'] + '-' + call['@date']
            calls[key] = call

group_key = lambda call: datetime.fromtimestamp(int(call['@date'])/1000).strftime('%Y-%m')
group_function = lambda calls: sum([int(c['@duration']) for c in calls])

call_groups = {}
for key, call in calls.items():
    key = group_key(call)
    if key not in call_groups:
        call_groups[key] = []
    call_groups[key].append(call)

groups = {}
for key, items in call_groups.items():
    groups[key] = group_function(items)

pprint.pprint(groups)

