import pyperclip as pc

#Copy Email
f = open('D://Emails_Droid.csv, 'r')
emails = f.readlines()
f.close()
pc.copy(emails[0])

emails = emails[1:]
f1 = open('D://Emails_Droid.csv', 'w')
f1.writelines(emails)
f1.close()
#Email Copied



