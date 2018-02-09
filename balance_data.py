import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

file_name = 'Training_array_9414.npy'
train_data = np.load(file_name)

##df = pd.DataFrame(train_data)
##print(len(train_data))
##print(df.head())
##print(Counter(df[1].apply(str)))
##
##lefts = []
##rights = []
##forwards = []
##slow = []
##
##shuffle(train_data)
##
##for data in train_data:
##    img = data[0]
##    choice = data[1]
##
##    if choice == [1,0,0]:
##        lefts.append([img, choice])
##    elif choice == [0,1,0]:
##        forwards.append([img, choice])
##    elif choice == [0,0,1]:
##        rights.append([img, choice])
##    elif choice == [0,0,0]:
##        slow.append([img, choice])
##    else:
##        print('no matches!')
##
##forwards = forwards[:len(lefts)][:len(rights)]
##lefts = lefts[:len(forwards)]
##rights = rights[:len(forwards)]
##slow = slow[:len(lefts)][:len(rights)]
##
##final_data = forwards + lefts + rights + slow
##
##shuffle(final_data)
##print(len(final_data))
##np.save('Balanced__'+file_name, final_data)


for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test', img)
    print(choice)
    cv2.waitKey(25)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
