import csv
import random as rand
import json

data = {}
departments = []


class department :
    def __init__(self,code,color):
        self.code = code
        self.color = color

def exist(num) :
    for i in range(len(departments)) :
        for j in range(len(departments[i])):
            if departments[i][j].code == code:
                return departments[i][j]
    return department(code,rand.randint(1,4))

def errors() : 
    errors = 0
    for i in range(len(departments)) :
        for j in range(1,len(departments[i])):
            dept = departments[i][j]
            if departments[i][0].color == dept.color:
                errors += 1
    return errors

with open('limitrophes.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        deps = []
        for code in row:
            if code != "":
                deps.append(exist(code))
        departments.append(deps)

best_color = 0
while errors() > 0:
    for i in range(len(departments)) :
        for j in range(1,len(departments[i])):
            dept = departments[i][j]
            if departments[i][0].color == dept.color :
                min_error= 1000
                for x in range(2):
                    dept.color = rand.randint(1,4)
                    if errors() < min_error :
                        best_color = dept.color
                        min_error = errors()
                    dept.color = best_color
                
    print("errors : ",errors()) 

data['departments'] = []
for i in range(len(departments)) :
    print(departments[i][0].code, end=" ")
    for j in range(len(departments[i])):
        data['departments'].append({
            "code" : "FR-"+departments[i][j].code,
            "color" : departments[i][j].color
        })
        print(departments[i][j].color,end=" ")
    print("")
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
