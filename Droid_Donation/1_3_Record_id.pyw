import pyperclip as pc


#ENTER USERNAME
with open('D://Data//Email_to_Username.data', 'a') as f_edit:
    ID = pc.paste()
    new_line = str(ID)
    f_edit.write(new_line)
 
