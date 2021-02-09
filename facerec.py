import numpy as np
import os
import sys
import cv2
import platform
import time
import json
import pyautogui
from colorama import Fore
import re
import requests
size = str(pyautogui.size())
faceCascade = cv2.CascadeClassifier(r'cascadexml/frontalface.xml')
# Eye recognition classifier
eyeCascade = cv2.CascadeClassifier(r'cascadexml/eye.xml')
mouthCascade = cv2.CascadeClassifier('cascadexml/mouth.xml')
def update():
    url = 'https://api.github.com/repos/FonderElite/facerecognition/commits'
    r = requests.get(url)
    data = r.text
    parsed = str(json.loads(data))
    committer = parsed.find("committer")
    if "2021-02-08T11:54:49Z" in parsed:
        print(wi + rd + 'No New Updates at the moment.')
    else:
        print(wi + gr + "There is an update!")
        print(wi + "Kindly check https://github.com/fonderelite/facerecognition")

def camera():
    print(wi + 'Checking Screen Size...')
    time.sleep(2)
    print(wi + "Screen-Size: " + wi + yl + size)
    print(wi + "Turning On Camera.")
    print(wi + rd + "Press ESC key to exit")
    cap = cv2.VideoCapture(0)
    while True:
      ret_val, img = cap.read()
      mirror = True
      if mirror:
         img = cv2.flip(img, 1)
         cv2.imshow('Video Test', img)
      if cv2.waitKey(1) == 27:
       sys.exit()
cv2.destroyAllWindows()

def facerec():
    cap = cv2.VideoCapture(0)
    ok = True
    result = []
    while ok:
        # Read the image in the camera, ok is the judgment parameter of whether the reading is successful
        ok, img = cap.read()
        # Convert to grayscale image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Face detection
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(32, 32)
        )

        # Eye detection based on face detection
        for (x, y, w, h) in faces:
            fac_gray = gray[y: (y + h), x: (x + w)]
            result = []
            eyes = eyeCascade.detectMultiScale(fac_gray, 1.3, 2)
            # Conversion of eye coordinates, changing relative position to absolute position
            for (ex, ey, ew, eh) in eyes:
                result.append((x + ex, y + ey, ew, eh))

        # Draw rectangle
        for (x, y, w, h) in faces:
           rect1 =  cv2.rectangle(img, (x, y), (x + w, y + h), (200, 100, 100), 2)
           cv2.putText(img, "Human", (x, y),  cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        for (ex, ey, ew, eh) in result:
          rect2 =   cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (255, 200, 100), 2)
          cv2.putText(img, "Eye", (ex, ey), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        cv2.imshow('video', img)
        k = cv2.waitKey(1)
        if k == 27:  # press 'ESC' to quit
            break



    cap.release()
    cv2.destroyAllWindows()

def quit():
    quitc = input(wi +  'Are you sure you want to quit?(y/n): ')
    if quitc == "y":
        print('Quitting...')
        time.sleep(1)
        print(wi + rd + '''
   __       __
o-''))_____//   
"--__/ * * * ) Woof Woof! 
c_c__/-c____/ Dont be a Script Kiddie
        ''')
        sys.exit()
    elif quitc == "n":
     print(wi +  rd + "Cancelled.")
    else:
     print(wi +  rd + "Exitting..")
     sys.exit()
osys = platform.system()
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#


try:
 import cv2
 import numpy
 import pyautogui
 import requests
 

except ImportError:
 print(rd + wi + "You Have Some Missing modules!")
 print(wi + 'Installing Missing Modules')
 os.system('pip3 install opencv-python')
 os.system('pip3 install numpy')
 os.system('pip3 install pyautogui')
 os.system('pip3 install requests')

help = wi + yl + '''
=============================================
+|  FaceRecognition By  Fonder-Elite       |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -fc         Face_Recognition       |+
+|      -c          Camera Check           |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+|Ex. ./facerec -fc -s (start)             |+
+|=========================================|+
'''
faceCascade = cv2.CascadeClassifier(r'C:/Users/Lenovo/Documents/frontalface.xml')
# Eye recognition classifier
eyeCascade = cv2.CascadeClassifier(r'C:/Users/Lenovo/Documents/eye.xml')
mouthCascade = cv2.CascadeClassifier('C:/Users/Lenovo/Documents/mouth.xml')
sys.stdout.write(wi + '\rLoading..')
time.sleep(1)
sys.stdout.write(wi + '\rLoading...')
time.sleep(1)
sys.stdout.write(wi +'\rLoading....')
time.sleep(1)
sys.stdout.write(wi +'\rLoading......')
time.sleep(1)
sys.stdout.write('\rLoading..........')
time.sleep(1)
flush = sys.stdout.flush()
banner = print(wi + Fore.CYAN + '''
       _______
     _/       \_
    / |       | |;
   /  |__   __|  |[
  |__/((o| |o))\__| Face Recognition 
  |      | |      | Using Python
  |\     |_|     /| 
  | \   ______  / | By FonderElite
   \| /  ___  \ |/
    \ | / _ \ | /
     \_________/
      _|_____|_
 ____|_________|____
/                   \  
______________________
''')

print(wi + yl + 'Created By FonderElite || Droid')
print(wi + yl  + 'Visit My GitHub Page: https://github.com/FonderElite')
print(wi + yl  + 'Visit my shop: https://legion.rf.gd')
print(wi + yl + '=======================================================')
print(wi + './facerec -h for help')
while True:
 cmd =  input(wi + gr + osys + "-User: ")
 if cmd == "./facerec -h":
   print(help)
 elif cmd == "./facerec":
   print(help)
 elif cmd == "./facerec -u":
   update()
 elif cmd == "./facerec -c":
    camera()
 elif cmd == "./facerec -fc -s":
    facerec()
 elif cmd == "./facerec -q":
    quit()
 else:
     print(wi + rd + '''
╦╗┬─┐┬ ┬  ┌─┐┌─┐┌─┐┬┌┐┌ 
 ║ ├┬┘└┬┘  ├─┤│ ┬├─┤││││ 
 ╩ ┴└─ ┴   ┴ ┴└─┘┴ ┴┴┘└┘o 
     ''')
#Dont be a script kiddie dummy
