# ✅ Install necessary libraries in GitHub Codespaces (Only required once)
try:
    import tensorflow as tf
    import tensorflow_datasets as tfds
    import numpy as np
    import matplotlib.pyplot as plt
    from tensorflow.keras.applications import EfficientNetB0
    from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
    from tensorflow.keras.models import Model
except ImportError:
    import os
    os.system("pip install tensorflow tensorflow-datasets numpy matplotlib")

import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.models import Model

# ✅ Check for GPU (Codespaces usually runs on CPU)
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("✅ GPU found:", gpus[0])
    tf.config.experimental.set_memory_growth(gpus[0], True)
else:
    print("❌ No GPU found. Running on CPU (Optimized for Codespaces).")

# ✅ Load PlantVillage Dataset (Use a smaller subset for fast execution)
dataset_name = "plant_village"
(train_data, val_data), dataset_info = tfds.load(
    dataset_name,
    split=["train[:20%]", "train[20%:30%]"],  # ✅ Load only 30% of the dataset
    as_supervised=True,
    with_info=True
)

# ✅ Get Number of Classes
num_classes = dataset_info.features["label"].num_classes
print(f"✅ Dataset Loaded: {num_classes} classes")

# ✅ Preprocess Data
IMG_SIZE = 128  
BATCH_SIZE = 8  
AUTOTUNE = tf.data.AUTOTUNE

def preprocess(image, label):
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)  # ✅ Use float32 for CPU compatibility
    return image, tf.one_hot(label, num_classes)

# ✅ Optimize Dataset Pipeline
train_data = (train_data.map(preprocess, num_parallel_calls=AUTOTUNE)
              .batch(BATCH_SIZE)
              .shuffle(500)
              .prefetch(AUTOTUNE))

val_data = (val_data.map(preprocess, num_parallel_calls=AUTOTUNE)
            .batch(BATCH_SIZE)
            .prefetch(AUTOTUNE))

# ✅ Reduce Dataset Size (Fast Execution)
train_data = train_data.take(2000)  # ✅ Use only 2000 samples
val_data = val_data.take(500)

# ✅ Load Smaller Model (EfficientNetB0)
base_model = EfficientNetB0(weights="imagenet", include_top=False, input_shape=(IMG_SIZE, IMG_SIZE, 3))
base_model.trainable = False  # ✅ Freeze base model to save training time

# ✅ Build the Model
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
x = Dropout(0.3)(x)
x = Dense(64, activation="relu")(x)
x = Dropout(0.3)(x)
predictions = Dense(num_classes, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=predictions)

# ✅ Compile the Model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
              loss="categorical_crossentropy",
              metrics=["accuracy"])

# ✅ Free Memory Before Training
import gc
tf.keras.backend.clear_session()
gc.collect()

# ✅ Train the Model (Fewer Epochs for Faster Execution)
EPOCHS = 5  # ✅ Reduce epochs for quick training
history = model.fit(train_data, validation_data=val_data, epochs=EPOCHS)

# ✅ Save Model (No Download Step in Codespaces)
model.save("crop_disease_model.h5")
print("✅ Model saved as crop_disease_model.h5")
