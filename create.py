import csv

with open('generic.csv',mode='r') as generic:
 reader = csv.reader(generic)
 for rows in reader:
  name = rows[0]
#   print(name)
  name= name.replace(" ", "_")
  name = name+".rst"
  print(name)
  f= open(name,"w+",encoding='utf-8')
  f.write("""
الاسم العلمي
=====





دواعي الاستعمال
=====






الاعراض الجانبية
=====






موانع الاستخدام
=====







الاستخدام اثناء الحمل
=====







الاسماء التجارية
=======







الجرعات والشكل الدوائي
======








المراجع
======






  """) 
  f.close()