from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


classifier = Sequential()


classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))


classifier.add(MaxPooling2D(pool_size=(2, 2)))


classifier.add(Conv2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))


classifier.add(Flatten())


classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=1, activation='sigmoid'))


classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])



from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory(r'C:\Users\bhava\OneDrive\Desktop\ad team 8\Fake-currency-detection-master\Indian Currency Dataset\train',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory(r'C:\Users\bhava\OneDrive\Desktop\ad team 8\Fake-currency-detection-master\Indian Currency Dataset\test',
                                            target_size=(64, 64),
                                            batch_size=16,
                                            class_mode='binary')

classifier.fit_generator(training_set,
                         steps_per_epoch=96,
                         epochs=4,
                         validation_data=test_set,
                         validation_steps= 13 )
classifier.save('currnencymodel.h5');

import numpy as np
from keras.preprocessing import image

##test_image = image.load_img(r'C:\Users\bhava\OneDrive\Desktop\ad team 8\Fake-currency-detection-master\Indian Currency Dataset\test\fake\test (14).jpg', target_size=(64, 64))
##test_image = image.img_to_array(test_image)
##test_image = np.expand_dims(test_image, axis=0)
##result = classifier.predict(test_image)
##training_set.class_indices
#if result[0][0] == 1:
 ##   prediction = 'Real'
#else:
 #   prediction = 'Fake'
#print("ans: ",prediction)