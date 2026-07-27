# 🧠 Brain Tumor Detection using CNN

A Deep Learning-based web application that detects different types of brain tumors from MRI images using a Convolutional Neural Network (CNN). The application is built with TensorFlow, Keras, and Streamlit.

---

## 📌 Project Overview

This project classifies brain MRI images into one of the following four categories:

- 🧠 Glioma Tumor
- 🧠 Meningioma Tumor
- 🧠 Pituitary Tumor
- ✅ No Tumor

The model is trained on MRI brain scan images and deployed using Streamlit for easy use through a web interface.

---

## 🚀 Features

- Upload Brain MRI Images
- CNN-based Classification
- Predicts Tumor Type
- Displays Prediction Confidence
- User-friendly Streamlit Interface
- Fast Real-Time Prediction
- Deep Learning Model (.keras)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| TensorFlow | Deep Learning |
| Keras | CNN Model |
| NumPy | Numerical Computing |
| Pillow | Image Processing |
| Streamlit | Web Application |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```
Brain_Tumor_Detection/
│
├── app.py
├── brain_tumor_model.keras
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Model Architecture

The CNN model consists of:

- Convolution Layers
- Max Pooling Layers
- Batch Normalization
- Dropout
- Dense Layers
- Softmax Output Layer

---

## 📊 Classes

| Class | Description |
|-------|-------------|
| Glioma | Brain Tumor |
| Meningioma | Brain Tumor |
| Pituitary | Brain Tumor |
| No Tumor | Healthy MRI |

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Nandini200506/Brain-Tumor-Detection.git
```

Move into the project folder

```bash
cd Brain-Tumor-Detection/Brain_Tumor_Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🖼️ How to Use

1. Launch the Streamlit application.
2. Upload a Brain MRI image.
3. Click the **Predict** button.
4. View the predicted tumor type.
5. Check the confidence score.

---

## 📦 Requirements

- Python 3.10+
- TensorFlow
- Streamlit
- NumPy
- Pillow

---

## 📈 Future Improvements

- Grad-CAM Visualization
- Better CNN Architecture
- Mobile Responsive UI
- Explainable AI
- Multi-language Support
- Cloud Deployment

---

## 👩‍💻 Developer

**Nandini Prajapati**

B.Tech – Computer Science (Artificial Intelligence)

Interested in:
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Data Science
- Computer Vision

GitHub:
https://github.com/Nandini200506

LinkedIn:
https://www.linkedin.com/in/nandini6032005/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is developed for educational and learning purposes.