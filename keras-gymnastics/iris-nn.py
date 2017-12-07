import numpy as np
from keras.models import Sequential
from keras.layers import Dense

import sys

from sklearn import datasets
from sklearn import metrics

# not interested in splitting into train/test cause i'm only
# interested in the mechanism of creating/training a NN with tensorflow
iris = datasets.load_iris()

# arranging the data for multi-class classification
X_train = iris.data
nFeatures = X_train.shape[1]
y_train_labels = iris.target
labels = np.unique(y_train_labels)
nLabels = len(labels)
y_train = np.zeros(shape=(y_train_labels.shape[0],nLabels))

for i in range(len(labels)):
    y_train[:,i][np.where(y_train_labels == labels[i])] = 1.0

# build the neural net
model = Sequential()
model.add(Dense(16,input_dim=4,activation='sigmoid'))
model.add(Dense(16,activation='sigmoid'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# and fit
model.fit(X_train, y_train, epochs=150, batch_size=10)


# and check our prediction. just using the train dataset for simplicity
prediction = np.argmax(model.predict(X_train),axis=1)

print(metrics.classification_report(y_train_labels,prediction))

