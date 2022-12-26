import pyperclip as pc
from datetime import datetime
#Copy Email
f = open('D://3_Email_Tech.csv', 'r')
emails = f.readlines()
email_id = emails[0].replace('\n', '')
f.close()

try:
    pc.copy(email_id)
except:
    import pyautogui as pg
    pg.press("esc")
    print('Done!')

f1 = open('D://3_Email_Tech.csv', 'w')
f1.writelines(emails[1:])
f1.close()
