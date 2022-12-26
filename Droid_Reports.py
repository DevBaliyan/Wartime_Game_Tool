import pyperclip as pc
import csv
import datetime
dt = datetime.datetime.now()


f = open("D://Data//Droid_Opening_Reports.csv", mode='a', newline='')
csvwriter = csv.writer(f)

d = dt.strftime("%d/%m/%y")         #Stores the Date
t = dt.strftime("%I:%M:%S %p")      #Stores the Time

data = ['twpg50@gmail.com', t, d]
csvwriter.writerow(data)


f.close()

print('Done!')



