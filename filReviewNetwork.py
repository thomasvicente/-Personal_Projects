import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

# dataset
(x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(num_words=10000)

# padding sequences to the same length
max_length = 500
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=max_length)
x_val = keras.preprocessing.sequence.pad_sequences(x_val, maxlen=max_length)

# Model
model = keras.Sequential()
model.add(keras.layers.Embedding(10000, 16))
model.add(keras.layers.LSTM(16, return_sequences=True))
model.add(keras.layers.GlobalMaxPool1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# training
model.fit(x_train, y_train, epochs=5, validation_data=(x_val, y_val))

# saving trained model
model.save('sentiment_analysis_model.h5')

# testing model
new_review = "The movie was great! I loved the acting and the plot."
new_review = keras.preprocessing.text.text_to_word_sequence(new_review)
new_review = keras.preprocessing.sequence.pad_sequences([new_review], maxlen=max_length)
prediction = model.predict(new_review)

# prediction output
print("Predicted sentiment: ", "Positive" if prediction[0] > 0.5 else "Negative")
