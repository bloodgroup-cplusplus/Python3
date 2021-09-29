# LOAD DATA
# first neural network with keras tutorial

import pandas as pd

import tensorflow as tf

from tensorflow import keras 

from tensorflow.keras import layers

dataset = pd.read_csv("diabetes.csv")

#Splitting the data into input(X) and output(y) variables 

X = dataset.iloc[:,0:8]

y= dataset.iloc[:,8]


# DEFINE KERAS MODEL 

model = keras.Sequential()

model.add(layers.Dense(12,input_dim =8,activation = 'relu'))

model. add(layers.Dense(8,activation = 'relu'))

model.add (layers.Dense(1,activation = 'sigmoid'))

#print(model.summary())

#print(model.weights)
#this prints weights and biases the last 1 is a bias 

# What weights has been assigned in the first layers

print(model.layers[0].get_weights())



print(10*"\n")

#print(model.layers[1].get_weights())


#print(10*"\n")
#print(model.layers[2].get_weights())


#print(10*"\n")

#print(model.layers[3].get_weight())
# What weights has been assigned in the second layers 

#print(model.layers[1].get_weights())


#print(model.layers[2].get_weights())

#COMPILE THE KERAS MODEL

model.compile(loss = 'binary_crossentropy', optimizer ='adam',metrics = ['accuracy'])

#EVALUATE KERAS MODEL
model.fit(X,y,epochs =150, batch_size = 10,verbose = 0)



_,accuracy= model.predict_classes(X)


# MAKE PREDICTIONS 

"AFter i train my model, how can I use it to make predictions on new data"

predictions = model.predict(X)

rounded = [round(x[0]) for x in predictions]

# make class predictions wit the model 




predictions = model.predict_classes(X)
