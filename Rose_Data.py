import pyperclip as pc
import csv
from datetime import datetime
dt = datetime.now()

f = open("D://Data//Rose_Data.csv", mode='a', newline='')
csvwriter = csv.writer(f)
t = dt.strftime("%I:%M:%S %p")
email = pc.paste()
email = email.replace("\n", '')
data = [email, t, 'Successful', open('D://delta.time', 'r').read()+'s']

csvwriter.writerow(data)
f.close()
