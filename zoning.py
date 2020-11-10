#!/usr/bin/env python3

import csv
from jinja2 import Environment, FileSystemLoader

ZonesetA='ZonesetA'
ZonesetB='ZonesetB'

with open('data/init-a.csv') as f:
    InitiatorA = [{k:v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

with open('data/target-a.csv') as f:
    TargetA = [{k:v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

with open('data/init-b.csv') as f:
    InitiatorB = [{k:v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

with open('data/target-b.csv') as f:
    TargetB = [{k:v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True

template = env.get_template('fabric.yml.j2')

with open('output/fabric-A.yml','w') as f:
    f.write(template.render(initiator=InitiatorA,target=TargetA,fabric='a',zoneset=ZonesetA))
    f.close()


with open('output/fabric-B.yml','w') as f:
    f.write(template.render(initiator=InitiatorB,target=TargetB,fabric='b',zoneset=ZonesetB))
    f.close()
