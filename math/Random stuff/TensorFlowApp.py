import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

x_inputs = np.array([-1.0, 0.0, 1.0, 2.0], dtype=float)
y_outputs = np.array([-4.0, -1.0, 2.0, 5.0], dtype=float)

model.fit(x_inputs, y_outputs, epochs=1000)

prediction = model.predict([5])
rounded_prediction = round(prediction[0][0], 2)  # Round to 2 decimal places

print("My prediction is:", rounded_prediction)
