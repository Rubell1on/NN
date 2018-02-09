import numpy as np
from PIL import ImageGrab
import pandas as pd
from collections import Counter
import cv2
import time
from getkeys import key_check
import os

width = 180
height = 140
i = 1

file_name = 'training_data_v2.npy'

if os.path.isfile(file_name):
    print('File exests, loadiong previous data!')
    training_data = np.load(file_name)
    
pic_size = training_data[0]
if pic_size[0].shape[0]!=height or pic_size[0].shape[1]!=width:
    for data in training_data:
        data[0] = cv2.resize(data[0], (width, height))
        choice = data[1]
        cv2.imshow('', data[0])
        print(choice, i, len(training_data))
        i=i+1
        if cv2.waitKey(25) & 0xFF == ord('q'):
           cv2.destroyAllWindows()
           break
    print('Converted!')
    if input('Save converted data?(y/n): ') == 'y':
        np.save('2_'+file_name, training_data)
        print('Saved!')
    else:
        print('Canceled')
else:
    print('data is correct!')
        
