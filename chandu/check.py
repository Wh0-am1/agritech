import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Paths to your dataset directories
data_dir = "C:\Users\chand\OneDrive\Documents\GitHub\agritech\Custom Dataset"
tender_dir = os.path.join(data_dir, "Tender")
mature_dir = os.path.join(data_dir, "Mature")

# Parameters
img_height, img_width = 150, 150
batch_size = 32
epochs = 10

# Data augmentation and preprocessing
data_gen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    horizontal_flip=True,
    rotation_range=20,
    zoom_range=0.2
)

train_data = data_gen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

val_data = data_gen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

# Building the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Training the model
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=epochs
)

# Save the model
model.save("coconut_classifier.h5")

# Load and test the model (optional)
# from tensorflow.keras.models import load_model
# model = load_model("coconut_classifier.h5")

# Predicting on a new image
def predict_image(image_path):
    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    import numpy as np

    img = load_img(image_path, target_size=(img_height, img_width))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    return "Tender" if prediction[0][0] < 0.5 else "Mature"

# Example usage
# result = predict_image("path/to/new/image.jpg")
# print("Prediction:", result)
