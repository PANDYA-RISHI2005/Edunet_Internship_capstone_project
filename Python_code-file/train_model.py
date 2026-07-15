import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping

IMAGE_SIZE = (128, 128)
BATCH_SIZE = 32

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True,
    width_shift_range=0.2,
    height_shift_range=0.2
)

train_data = train_datagen.flow_from_directory(
    "dataset",
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    subset="training",
    shuffle=True
)

val_data = train_datagen.flow_from_directory(
    "dataset",
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    subset="validation",
    shuffle=False
)

print("Class Indices:")
print(train_data.class_indices)

model = models.Sequential([

    layers.Input(shape=(128,128,3)),

    layers.Conv2D(32,(3,3),activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(64,(3,3),activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(128,(3,3),activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),

    layers.Dense(128,activation="relu"),
    layers.Dropout(0.5),

    layers.Dense(train_data.num_classes,activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=25,
    callbacks=[early_stop]
)

model.save("eco_scan_model.h5")

print("Model Saved Successfully")