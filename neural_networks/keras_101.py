
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np
np.random.seed(9)
sgd = optimizers.SGD(lr=1)

model = Sequential()

# add layers
# layer 1
# input_dim = features e.g. columns
model.add(Dense(units=4, activation='sigmoid', input_dim=3))
# Layer 2
# Output Layer
model.add(Dense(units=1,activation='sigmoid'))

print(model.summary())
model.compile(loss='mean_squared_error', optimizer=sgd)
# ensures reproducible results

X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
y = np.array([[0],[1],[1],[0]])

model.fit(X, y, epochs=1500, verbose=False)

print(model.predict(X))
