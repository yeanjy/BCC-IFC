import datetime
data = datetime.datetime.now()
data1 = data.strftime ("%d/%m/%y")
hora = data.strftime ("%H:%M:%S")
print (data1)
print (hora)