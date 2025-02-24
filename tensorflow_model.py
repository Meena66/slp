import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, LearningRateScheduler
import numpy as np

# Custom learning rate scheduler
def lr_schedule(epoch, lr):
    if epoch > 10:
        lr = lr * 0.1  # Reduce the learning rate after 10 epochs
    return lr

def create_tensorflow_model(input_dim):
    model = Sequential()

    # Input layer with Batch Normalization
    model.add(Dense(128, input_dim=input_dim, activation='relu'))
    model.add(BatchNormalization())

    # Hidden layers with Dropout and Batch Normalization
    model.add(Dense(128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    model.add(Dense(64, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    # Output layer (3 classes: obstructive, central, complex apnea)
    model.add(Dense(3, activation='softmax'))

    # Compile the model with custom optimizer and metrics
    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    return model

# Function to train the model
def train_tensorflow_model(X_train, y_train, epochs=30, batch_size=32):
    model = create_tensorflow_model(X_train.shape[1])

    # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    # Model checkpoint to save the best model
    model_checkpoint = ModelCheckpoint('best_sleep_apnea_model.h5', save_best_only=True, monitor='val_accuracy', mode='max')

    # Learning rate scheduler
    lr_scheduler = LearningRateScheduler(lr_schedule)

    # Train the model with early stopping and model checkpointing
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2,
              callbacks=[early_stopping, model_checkpoint, lr_scheduler])

    # Save the final model after training
    model.save('final_sleep_apnea_model.h5')
    
    return model

# Function to predict apnea type using the trained TensorFlow model
def predict_sleep_apnea(model, X_test):
    predictions = model.predict(X_test)
    predicted_class = np.argmax(predictions, axis=1)  # Returns the class with the highest probability
    return predicted_class
