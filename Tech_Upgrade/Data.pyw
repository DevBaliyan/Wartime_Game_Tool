import pytesseract
from PIL import ImageGrab
import pyperclip as pc


pytesseract.pytesseract.tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'


img1 =  ImageGrab.grab(bbox=(92,77,155,93))
img2 =  ImageGrab.grab(bbox=(197,77,254,93))
img3 =  ImageGrab.grab(bbox=(262,149,346,173))

text1 = (pytesseract.image_to_string(img1)).replace('\n\x0c', '')
text2_temp, text2 = (pytesseract.image_to_string(img2)).replace('\n\x0c', ''), ''
text3 = (pytesseract.image_to_string(img3)).replace('\n\x0c', '')

mail = pc.paste()
name = mail.replace('@gmail.com', '')
img1.save('D://Data//temp//Gold//'+name+'.png')
img2.save('D://Data//temp//Gems//'+name+'.png')
img3.save('D://Data//temp//Exp//'+name+'.png')

for i in text2_temp:
    if i.isdigit() == True:
        text2 += i

with open("D://Data.csv", 'a') as file:
    file.write(mail+','+text1+','+text2+','+text3+'\n')
