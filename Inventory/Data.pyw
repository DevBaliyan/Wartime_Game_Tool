from PIL import ImageGrab
import pyperclip as pc
import pyautogui as pg
import cv2 as cv
import keyboard


def coord_shard():
    global img_shard
    coord = pg.locateCenterOnScreen(img_shard, confidence=0.7)
    return coord

def coord_gold():
    global img_gold
    coord = pg.locateCenterOnScreen(img_gold, confidence=0.7)
    return coord


#Names
mail = pc.paste()
name = mail.replace('@gmail.com', '')


img_shard = cv.imread('D://Data//Shard.png')
img_gold = cv.imread('D://Data//Gold.png')


while True:
    keyboard.wait('q')
    coord1, coord2 = coord_shard(), coord_gold()
    try:
        a, b = coord1
        img1 =  ImageGrab.grab(bbox=(a, b+15, a+30, b+33))
    except:
        img1 = ImageGrab.grab(bbox=(100,100,110,110))

    try:
        x, y = coord2
        img2 = ImageGrab.grab(bbox=(x+5, y+28, x+42, y+43))
    except:
        img2 = ImageGrab.grab(bbox=(100,100,110,110))

    img1.save('D://Data//temp//Shard//'+name+'.png')
    img2.save('D://Data//temp//Gold//'+name+'.png')
    coord1, coord2 = None, None
    keyboard.write('Continue')
