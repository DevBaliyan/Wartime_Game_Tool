import pyperclip as pc
import csv
import datetime
dt = datetime.datetime.now()

f = open("D://Data//Join_Alliance.csv", mode='a', newline='')
csvwriter = csv.writer(f)
t = dt.strftime("%I:%M:%S %p")
email = pc.paste()
email = email.replace("\n", '')
data = [email, t, 'Successful']

csvwriter.writerow(data)
f.close()
