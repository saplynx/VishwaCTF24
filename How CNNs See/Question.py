from tensorflow import keras


from keras.models import load_model

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import cv2

model = load_model('./NumberRecognizer.h5')

img = cv2.imread("./Test_Images/Images/2.png")

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
image = [image]

image = np.expand_dims(image, axis=-1)
predictions= np.argmax(model.predict(image))
plt.imshow(np.squeeze(image), cmap='gray')
plt.title(f'Predicted Value : {predictions}')

plt.show()