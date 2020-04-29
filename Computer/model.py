__author__ = 'Ayush Singh'

import cv2
import numpy as np
import glob
import sys
import time
import os
from sklearn.model_selection import train_test_split
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from sklearn.model_selection import train_test_split
from keras.models import Sequential, save_model
import matplotlib.pyplot as plt
from numpy import newaxis
from keras.models import load_model




def load_data(input_size, path):
    print("Loading training data...")
    start = time.time()

    # load training data
    X = np.empty((0, input_size))
    y = np.empty((0, 4))
    training_data = glob.glob(path)

    # if no data, exit
    if not training_data:
        print("Data not found, exit")
        sys.exit()

    for single_npz in training_data:
        with np.load(single_npz) as data:
            train = data['train']
            train_labels = data['train_labels']
        X = np.vstack((X, train))
        y = np.vstack((y, train_labels))

    print("Image array shape: ", X.shape)
    print("Label array shape: ", y.shape)

    end = time.time()
    print("Loading data duration: %.2fs" % (end - start))

    # normalize data
    #X = X / 255.
    
    # NEW EDITS
    IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 192, 320, 1
    INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)


    data_abc = np.empty( [X.shape[0], IMAGE_HEIGHT, IMAGE_WIDTH ], dtype='uint8' )
    for i in range(X.shape[0],):
        data_abc[i]= np.reshape(X[i],(-1,320))
    #print(data_abc.shape)
    data_X=data_abc[:,:,:,newaxis]

    #print(data_X.shape)
    
    
    # train validation split, 7:3
    return train_test_split(data_X, y, test_size=0.3)


class NeuralNetwork(object):
    def __init__(self):
        self.model = Sequential()

    def create(self):
        # create neural network
        IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 192, 320, 1
        INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)
        #self.model = cv2.ml.ANN_MLP_create()
        #self.model.setLayerSizes(np.int32(layer_sizes))
        #self.model.setTrainMethod(cv2.ml.ANN_MLP_BACKPROP)
        #self.model.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM, 2, 1)
        #self.model.setTermCriteria((cv2.TERM_CRITERIA_COUNT, 100, 0.01))

        
        self.model = Sequential()
        self.model.model.add(Conv2D(24, 5, 5, activation='relu',input_shape = INPUT_SHAPE, subsample=(2, 2)))

        self.model.add(Conv2D(36, 5, 5, activation='relu', subsample=(2, 2)))


        self.model.add(Conv2D(48, 5, 5, activation='relu', subsample=(2, 2)))


        self.model.add(Conv2D(64, 3, 3, activation='relu'))


        self.model.add(Conv2D(64, 3, 3, activation='relu'))


        self.model.add(Dropout(0.5))


        self.model.add(Flatten())


        self.model.add(Dense(100, activation='relu'))


        self.model.add(Dense(50, activation='relu'))


        self.model.add(Dense(10, activation='relu'))


        self.model.add(Dense(4))

        self.model.summary()
           
    def train(self, X_train, Y_train, X_test, Y_test):
        # set start time
        start = time.time()

        print("Training ...")
        #self.model.train(np.float32(X), cv2.ml.ROW_SAMPLE, np.float32(y))
        checkpoint = ModelCheckpoint('model-{val_loss:.4f}.h5',monitor='val_loss',verbose=0,save_best_only=True,mode='auto')
        self.model.compile(loss='mean_squared_error', optimizer=Adam(lr=1.0e-4),metrics=['accuracy'])
        self.model.fit( X_train, Y_train, batch_size=32, nb_epoch=30, validation_data=(X_test, Y_test),callbacks=[checkpoint], shuffle=True )
        # set end time
        end = time.time()
        print("Training duration: %.2fs" % (end - start))

    def evaluate(self, X, y):
        ynew=self.model.predict(X)
        for i in range(len(X)):
            print("X=%s, Predicted=%s" % (X[i], ynew[i]))  
        #ret, resp = self.model.predict(X)
        a_prediction = ynew.argmax(-1)
        a_true_labels = y.argmax(-1)
        accuracy = np.mean(a_prediction == a_true_labels)
        print ('Train accuracy: ', "{0:.2f}%".format(accuracy * 100))
        return accuracy

    def save_model(self, path):
        directory = "saved_model"
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.model.save(path)
        print("Model saved to: " + "'" + path + "'")


    def load_model(self, path):
        print("load started")
        if not os.path.exists(path):
            print("Model 'nn_model.xml' does not exist, exit")
            sys.exit()
        #self.model = cv2.ml.ANN_MLP_load(path)
        #self.model.load_weights(path)
        #self.model = self.create()
        self.model=load_model(path)
        #print("load done")
        self.model.compile(loss='mean_squared_error', optimizer=Adam(lr=1.0e-4))
        #print("compile done")
        first_layer_weights = self.model.layers[0].get_weights()[0]
        #print(first_layer_weights)
        #print("loads check done")


        
    def predict(self, X):
        #print("pri")
        #print(X.shape)
        X=X[newaxis,:,:,newaxis]
        #print(data_X.shape)
        resp = self.model.predict(X)
        print(resp)
        return resp.argmax(-1)

