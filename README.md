# Crop_disesase_model


🌾 Crop Disease Detection Model
A deep learning model built with TensorFlow and EfficientNetB0 to classify crop diseases using the PlantVillage dataset. Optimized for GitHub Codespaces.

📌 Features
✅ Pretrained Model – Uses EfficientNetB0 for feature extraction.
✅ Optimized for GitHub Codespaces – Runs efficiently on CPU.
✅ Dataset Subset for Faster Training – Loads 30% of the dataset.
✅ Preprocessing & Augmentation – Includes resizing, one-hot encoding, and batching.
✅ Memory Optimization – Uses float32 precision for better CPU performance.
✅ Trained Model Saved – Exports crop_disease_model.h5 after training.

⚡ Installation
Before running the model, install the required dependencies:


pip install tensorflow tensorflow-datasets numpy matplotlib
🚀 Running the Model
Execute the Python script in GitHub Codespaces:


python Crop_disease.py

🛠 Project Workflow
1️⃣ Install Dependencies – TensorFlow, TensorFlow Datasets, NumPy, and Matplotlib.
2️⃣ Check GPU Availability – Defaults to CPU if no GPU is detected.
3️⃣ Load the PlantVillage Dataset – Uses only 30% for faster execution.
4️⃣ Preprocess Data – Resize images, normalize, and apply one-hot encoding.
5️⃣ Optimize Data Pipeline – Implements batching and prefetching.
6️⃣ Model Architecture – Uses EfficientNetB0 with custom Dense & Dropout layers.
7️⃣ Training the Model – Runs for 5 epochs to optimize performance.
8️⃣ Save the Model – Exports crop_disease_model.h5.

📊 Training Output
The model prints accuracy and loss metrics during training.
After successful training, the following message confirms the model is saved:


✅ Model saved as crop_disease_model.h5

👨‍💻 About the Developer
This project is developed as part of a deep learning and AI-based research initiative. Contributions and improvements are welcome!

Feel free to fork this repository, experiment with the model, and enhance its performance. 🚀

