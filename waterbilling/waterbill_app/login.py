import csv
mainsign=False

while mainsign==False
    data=[]
    with open("csv/consumerlist.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
