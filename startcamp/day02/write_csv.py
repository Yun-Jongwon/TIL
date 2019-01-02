lunch={
    '김밥':'054-555-5555',
    '햄버거':'054-777-7777',
    '돈가스':'054-111-1111'
    }

import csv

with open('lunch.csv','w',encoding='utf8',newline='') as f :
    csv_writer=csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)
        #f.write(f'{item[0]},{item[1]}\n')




