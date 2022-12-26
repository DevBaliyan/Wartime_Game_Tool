import pyperclip as pc
import csv, time
import datetime
dt = datetime.datetime.now()

f = open("D:\\Data\\Joined_Alliance_Already.csv", mode='a', newline='')
csvwriter = csv.writer(f)
t = dt.strftime("%I:%M:%S %p")
email = pc.paste()
email = email.replace("\n", '')
data = [email, t, 'Successful']

csvwriter.writerow(data)
f.close()
time.sleep(5)
