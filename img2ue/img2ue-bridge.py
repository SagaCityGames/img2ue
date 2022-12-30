#ONLY for Windows (pag.hotkey)
#ONLY to be called from terminal (not within UE)
# TO RUN CORRECTLY: Have Bridge window inactive but positioned on main tab so it will take up whole screen
#ref: https://www.youtube.com/watch?v=1RE5tSPO2RI
#ref: https://www.youtube.com/watch?v=eLw1dKSxVkE

#import unreal
from typing import Type
import pyautogui as pag
from time import sleep
import pyperclip
from tkinter import *
from tkinter import messagebox

delayShort = 1
delayMedium = 5
delayLong = 10

pag.locateOnScreen('img/UEWindow_Bridge_Inactive.png', grayscale = 'True') # locate and click on Bridge window
pag.click('img/UEWindow_Bridge_Inactive.png') # for exact dimension, pag.click(280,74)

f = open('test.txt', 'r') # search each word in file
for word in f:

    #pag.locateOnScreen('img/UEWindow_Bridge_Home.png') # filter for "3D Assets"
    #pag.click('img/UEWindow_Bridge_Home.png')
    #pag.move(50, -20)
    #pag.click()
    pag.move(200, 50)
    pag.click()
    # pag.locateOnScreen('img/UEWindow_Bridge_Search.png', grayscale = 'True')
    # pag.click('img/UEWindow_Bridge_Search.png')
    # pag.hotkey("ctrl", "v") # paste from clipboard

    #RESET SEARCH
    backspaces = 0
    while backspaces < 5:
        pag.press("backspace") # clear any text from previous search
        sleep(delayShort)
        backspaces = backspaces + 1
    backspaces = 0
    sleep(delayShort)

    #SEARCH FOR ASSET
    pag.typewrite("3d asset") # filter for 3d assets
    pag.press("enter")
    sleep(delayShort)
    pag.typewrite(word) # search word
    pag.press("enter")
    sleep(delayMedium)
    #pag.locateOnScreen('img/UEWindow_Bridge_LatestAssets.png') # 
    pag.click('img/UEWindow_Bridge_LatestAssets.png') # find asset to download
    pag.move(0, 50)
    pag.click()
    sleep(delayShort)

    try:
        #DOWNLOAD ASSET
        pag.locateOnScreen('img/UEWindow_Bridge_Download.png') # download asset
    except TypeError:
        search()
    else:
        pag.click('img/UEWindow_Bridge_Download.png')
        #TODO: handle if asset already downloaded
        sleep(5)
    finally:
        BridgeImport()

def BridgeImport():
    #IMPORT ASSET
    try:
        pag.locateOnScreen('img/UEWindow_Bridge_Add.png') # download asset
    except TypeError:
    
    else:
        pag.click('img/UEWindow_Bridge_Add.png')
        sleep(5)

    pag.locateOnScreen('img/UEWindow_Bridge_Inactive.png') # locate and click on Bridge tab
    pag.click('img/UEWindow_Bridge_Inactive.png')

#show window when script completed
window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
messagebox.showinfo('Script completed', 'img2ue-bridge completed.')
window.deiconify()
window.destroy()
window.quit()

f.close() # close file

#try: 
#except TypeError: # not found   
#else: # found
#finally: # rest of program

#pag.hotkey("ctrl", "p") # open UE asset picker