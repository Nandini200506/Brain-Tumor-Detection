import os
import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model

# ==========================================================
# Configuration
# ==========================================================

MODEL_PATH = os.path.join(os.path.dirname(__file__), "brain_tumor_model.keras")

CLASSES = [
    "Glioma",
    "Meningioma",
    "No Tumor",
    "Pituitary"
]

IMG_SIZE = (224, 224)

st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="centered"
)

# ==========================================================
# Load Model
# ==========================================================

@st.cache_resource
def get_model():
    return load_model(MODEL_PATH)

try:
    model = get_model()
except Exception as e:
    st.error("❌ Unable to load the model.")
    st.error(e)
    st.stop()

# ==========================================================
# Title
# ==========================================================

st.title("🧠 Brain Tumor Detection using CNN")

st.markdown("""
Upload a **Brain MRI Image** and the trained CNN model will classify it into one of the following categories:

- 🟢 No Tumor
- 🔴 Glioma
- 🟡 Meningioma
- 🟣 Pituitary
""")

# ==========================================================
# Upload Image
# ==========================================================

uploaded_file = st.file_uploader(
    "Choose an MRI Image",
    type=["jpg", "jpeg", "png"]
)

# ==========================================================
# Prediction
# ==========================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded MRI Image",
        use_container_width=True
    )

    img = image.resize(IMG_SIZE)

    img = np.array(img)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    if st.button("🔍 Predict"):

        with st.spinner("Analyzing MRI Scan..."):

            prediction = model.predict(img, verbose=0)

        predicted_index = np.argmax(prediction)

        predicted_class = CLASSES[predicted_index]

        confidence = prediction[0][predicted_index] * 100

        st.success(f"### Prediction: {predicted_class}")

        st.write(f"### Confidence: {confidence:.2f}%")

        st.progress(float(confidence / 100))

        st.subheader("Prediction Probabilities")

        for cls, prob in zip(CLASSES, prediction[0]):
            st.write(f"**{cls}** : {prob * 100:.2f}%")

        st.balloons()

else:
    st.info("📤 Upload an MRI image to start prediction.")

# ==========================================================
# Footer
# ==========================================================

st.markdown("---")

st.caption(
    "Developed using TensorFlow, CNN, Streamlit and Python."
)