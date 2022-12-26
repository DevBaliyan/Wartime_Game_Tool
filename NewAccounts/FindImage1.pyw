#from PIL import ImageGrab
import pyautogui as pg
import cv2 as cv
import keyboard
attempt = 0


def coord_sample(image):
    global attempt
    coord = pg.locateCenterOnScreen(image, confidence=0.8)
    attempt += 1
    print(attempt)
    if coord != None or attempt > 30:
        attempt = 0
        if coord != None:
            pg.moveTo(coord)
            keyboard.write('Continue1')
        else:
            keyboard.send('ctrl+c')
        return
    else:
        pg.sleep(0.45)
        coord_sample(image)


#Names
#mail = pc.paste()
#name = mail.replace('@gmail.com', '')


img_sample1 = cv.imread('E://Images4NewAccounts//Sample1.png')
#img_gold = cv.imread('D://Data//Gold.png')

keyboard.wait('Q')
coord_sample(img_sample1)

keyboard.wait('Q')
coord_sample(img_sample1)

keyboard.wait('Q')
coord_sample(img_sample1)

print("Execution Completed!!!")
