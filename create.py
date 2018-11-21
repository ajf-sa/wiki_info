import csv

with open('generic.csv',mode='r') as generic:
 reader = csv.reader(generic)
 for rows in reader:
  name = rows[0]
#   print(name)
  name= name.replace(" ", "_")
  name = name+".md"
  print(name)
  f= open(name,"w+")
  f.close()