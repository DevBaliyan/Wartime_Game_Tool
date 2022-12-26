import pyperclip as pc
from datetime import datetime

#Location
loc = 'D://1_Email_Join.csv' #Join

#Copy Email
f = open(loc, 'r')
emails = f.readlines()
email_id = emails[0].replace('\n', '')
f.close()

try:
    pc.copy(email_id)
except:
    import pyautogui as pg
    pg.press("esc")
    print('Done!')

f1 = open(loc, 'w')
f1.writelines(emails[1:])
f1.close()
#Email Copied
"""
#Part Time Job
with open('D://Data//Email_to_Username.data', 'a') as f_edit:
        f_edit.write(email_id+', ')"""

