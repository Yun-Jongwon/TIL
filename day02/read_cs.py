import csv

with open('lunch.csv','r',encoding='utf8')as f:
    #lines=f.readlines()
    
    items = csv.reader(f)

    print(items)
    for line in items:
        print(line)