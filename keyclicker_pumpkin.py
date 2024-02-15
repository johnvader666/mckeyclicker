import time
import sys
import pyautogui
import pyperclip
import random
from multiprocessing import Process


def getY ():
    pyautogui.keyDown('F3')
    time.sleep(0.2)
    pyautogui.press('c')
    pyautogui.keyUp('F3')
    clipText = pyperclip.paste()
    yRight = 4
    posVector = clipText.rsplit(" ", yRight)
    y = float(posVector[1])
    return y

def mcCommand ():
    loadingtime1 = random.uniform(0.4,0.5)
    loadingtime2 = random.uniform(3,4)
    pyautogui.press('t')
    pyautogui.write("/spawn")
    pyautogui.press('Enter')
    time.sleep(120)
    pyautogui.press('t')
    pyautogui.write("/play skyblock")
    pyautogui.press('Enter')
    time.sleep(loadingtime2)
    pyautogui.press('t')
    pyautogui.write("/warp garden")
    pyautogui.press('Enter')
    time.sleep(loadingtime2)
    pyautogui.press('r')

def serverDisconnect ():
    time.sleep(3)
    pyautogui.press('r')
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(959, 655)
    time.sleep(1)
    pyautogui.press('r')
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(1204, 335)
    pyautogui.press('r')
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(0.1)
    pyautogui.click(button='left')
    pyautogui.moveTo(1274, 866)
    time.sleep(20)
    pyautogui.press('r')
    pyautogui.click(button='left')
    time.sleep(25)
    mcCommand()


def myKeyClicker():
    while True:
        firstruntime = 10800
        startime = time.time()
        currentruntime = 0
        pyautogui.press('r')
        pyautogui.keyDown('ctrl')
        time.sleep(1)
        pyautogui.keyUp('ctrl')
        pyautogui.mouseDown(button='left')
        while currentruntime < firstruntime:
            waitingtimeD1 = random.uniform(10.5,11)
            waitingtimeD2 = random.uniform(10.5,11)
            waitingtimeD3 = random.uniform(10.5,11)
            waitingtimeD4 = random.uniform(10.5,11)
            waitingtimeA1 = random.uniform(10.5,11)
            waitingtimeA2 = random.uniform(10.5,11)
            waitingtimeA3 = random.uniform(10.5,11)
            waitingtimeA4 = random.uniform(10.5,11)
            waitingtimeW1 = random.uniform(1.8,2)
            waitingtimeW2 = random.uniform(1.8,2)
            waitingtimedebugW1 = random.uniform(0.5,0.6)
            waitingtimedebugW2 = random.uniform(0.5,0.6)
            waitingtimedebugW3 = random.uniform(0.5,0.6)
            waitingtimedebugW5 = random.uniform(0.5,0.6)
            waitingtimedebugW6 = random.uniform(0.5,0.6)
            waitingtimedebugW7 = random.uniform(0.5,0.6)
            pyautogui.keyDown('a')
            time.sleep(waitingtimeA1)
            pyautogui.keyDown('w')
            time.sleep(waitingtimedebugW1)
            pyautogui.keyUp('w')
            time.sleep(waitingtimeA2)
            pyautogui.keyDown('w')
            time.sleep(waitingtimedebugW2)
            pyautogui.keyUp('w')
            time.sleep(waitingtimeA3)
            pyautogui.keyDown('w')
            time.sleep(waitingtimedebugW3)
            pyautogui.keyUp('w')
            time.sleep(waitingtimeA4)
            pyautogui.keyUp('a')
            pyautogui.keyDown('w')
            time.sleep(waitingtimeW1)
            pyautogui.keyUp('w')
            pyautogui.keyDown('d')
            time.sleep(waitingtimeD1)
            pyautogui.keyDown('w')
            time.sleep(waitingtimedebugW5)
            pyautogui.keyUp('w')
            time.sleep(waitingtimeD2)
            pyautogui.keyDown('w')
            time.sleep(waitingtimedebugW6)
            pyautogui.keyUp('w')
            time.sleep(waitingtimeD3)
            pyautogui.keyDown('w')
            time.sleep(waitingtimedebugW7)
            pyautogui.keyUp('w')
            time.sleep(waitingtimeD4)
            pyautogui.keyUp('d')
            pyautogui.keyDown('w')
            time.sleep(waitingtimeW2)
            pyautogui.keyUp('w')
            currentruntime = time.time() - startime
        serverDisconnect()
        time.sleep(60)

if __name__ == '__main__':

    while True:
        yLimit = 68.00
        y = 1
        time.sleep(2)
        #start keyclicker ....
        # Create a new process
        keyClickerProcess = Process(target=myKeyClicker)
        keyClickerProcess.start()
        if keyClickerProcess.is_alive():
            print("Process successfully started.")
        else:
            print("Process start failed")
            sys.exit(1)

        while y < yLimit:
            time.sleep(6)
         
            try:
                y = getY()
            except Exception as e: 
                time.sleep(1)
                try:
                    y = getY()
                except Exception as e2:
                    #terminate everything...
                    print("Failed to get y pos second time! Disconnect started.") 
                    keyClickerProcess.terminate() 
                    serverDisconnect()
                    time.sleep(60)
                    break
        else:
            # y > limit!
            #stop keyclicker
            keyClickerProcess.terminate() 
            if not keyClickerProcess.is_alive():
                print("successfully Terminated")  
            else:
                print("Termination Failed")
            #enter command in minecraft
            mcCommand()
            #wait a few seconds
            time.sleep(2)