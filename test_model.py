import numpy as np
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from alexnet import alexnet
from getkeys import key_check
from PIL import ImageGrab

import random

WIDTH = 180
HEIGHT = 140
LR = 1e-3
EPOCHS = 10
MODEL_NAME ='pymw-car-0.001-alexnetv2-10-epochs-data_02112017.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.1

def cls():
    print('\n' * 50)

def straight():
##    if random.randrange(4) == 2:
##        ReleaseKey(W)
##    else:
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(W)
    PressKey(A)
    #ReleaseKey(W)
    ReleaseKey(D)
    #ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(A)

def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    #ReleaseKey(W)
    #ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(D)

def releaseAll():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    
model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(2))[::-1]:
        print(i+1)
        time.sleep(1)

    turn_thresh = 0.85
    fwd_thresh = 0.7

    paused = False
    while(True):
        
        if not paused:
            # 800x600 windowed mode
            screen =  np.array(ImageGrab.grab(bbox=(100,100,900,700)))
            #screen = grab_screen(region=(100,100,900,700))
            
            print('loop took {} seconds'.format(time.time()-last_time), '\t',  'fwd_thresh=', round(fwd_thresh,2), ' ', 'turn_thresh=', round(turn_thresh,2))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (180,140))

            prediction = model.predict([screen.reshape(180,140,1)])[0]
            print(prediction)
            #cls()
            

            if prediction[1] > fwd_thresh:
                straight()
            elif prediction[0] > turn_thresh:
                left()
            elif prediction[2] > turn_thresh:
                right()
            else:
                releaseAll()

        keys = key_check()

        # p pauses game and can get annoying.
        if '1' in keys:
            if fwd_thresh > 0.05:
                fwd_thresh = fwd_thresh - 0.05
        elif '2' in keys:
            if fwd_thresh < 0.95:
                fwd_thresh = fwd_thresh + 0.05

        if '3' in keys:
            if turn_thresh > 0.05:
                turn_thresh = turn_thresh - 0.05
        elif '4' in keys:
            if turn_thresh < 0.95:
                turn_thresh = turn_thresh + 0.05
        
                
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

main()       
