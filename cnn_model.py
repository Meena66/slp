import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

def create_cnn_model(input_shape):
    model = Sequential()

    # Adding Conv1D layers for pattern detection
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=input_shape))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(filters=128, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(filters=256, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))

    # Flatten the output for dense layers
    model.add(Flatten())

    # Fully connected layers
    model.add(Dense(512, activation='relu'))
    model.add(Dense(3, activation='softmax'))  # 3 classes: obstructive, central, complex apnea

    # Compile the model
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    return model

# Function to train the model
def train_cnn_model(X_train, y_train, epochs=10, batch_size=32):
    model = create_cnn_model((X_train.shape[1], X_train.shape[2]))  # input shape based on data
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    model.save('cnn_breathing_model.h5')  # Save the trained model
    return model

# Function to predict apnea using the trained CNN model
def predict_breathing_pattern(model, X_test):
    predictions = model.predict(X_test)
    return predictions
