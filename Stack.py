import numpy as np
import cv2

data_1 = 'Stacked_Balanced3train_vity10.npy'
data_2 = 'Balanced__31102017_3.npy'

training_data_1 = np.load(data_1)
training_data_2 = np.load(data_2)
print(training_data_1[0][0].shape, training_data_2[0][0].shape)
arr1 = []

arr1 = np.vstack((training_data_1, training_data_2))
print(len(training_data_1), len(training_data_2), len(arr1))
input()
##for data in arr1:
##    print(data[1])
##    cv2.imshow('test',data[0])
##    if cv2.waitKey(25) & 0xFF == ord('q'):
##        cv2.destroyAllWindows()
##        break
np.save('Stacked_'+ data_1, arr1) 
print('Saved!!!')






