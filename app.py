import streamlit as st
from PIL import Image
import random

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

# ---------------- CUSTOM DESIGN ----------------

st.markdown(
    """
    <style>
    .main {
        background-color: #f4fff4;
    }

    .title {
        color: #236b35;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #555555;
        font-size: 18px;
    }

    .box {
        padding: 20px;
        border-radius: 12px;
        background-color: #ffffff;
        border: 1px solid #d5ead5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------

st.markdown(
    '<div class="title">🌿 Plant Disease Detection</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Computer Vision Based Plant Health Analysis</div>',
    unsafe_allow_html=True
)

st.write("")

st.info(
    "Upload a plant leaf image to check its possible health condition."
)

# ---------------- MODULE 1 ----------------

st.header("📷 Module 1: Upload Leaf Image")

uploaded_file = st.file_uploader(
    "Select a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Plant Leaf",
        use_container_width=True
    )

    # ---------------- MODULE 2 ----------------

    st.header("🔍 Module 2: Image Analysis")

    st.success("Image uploaded successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Image Format**")
        st.write(image.format)

    with col2:
        st.write("**Image Size**")
        st.write(str(image.size))

    # ---------------- MODULE 3 ----------------

    st.header("🩺 Module 3: Prediction Result")

    if st.button("Analyze Plant Leaf"):

        result = random.choice(
            [
                "Healthy Leaf",
                "Possible Early Blight",
                "Possible Leaf Spot Disease"
            ]
        )

        if result == "Healthy Leaf":

            st.success("🌱 Prediction: Healthy Leaf")

            st.write(
                "The leaf appears healthy in this prototype."
            )

            st.write(
                "Suggested action: Continue regular watering "
                "and provide sufficient sunlight."
            )

        elif result == "Possible Early Blight":

            st.warning("⚠️ Prediction: Possible Early Blight")

            st.write(
                "The image may show symptoms similar to early blight."
            )

            st.write(
                "Suggested action: Inspect the plant carefully "
                "and remove affected leaves if required."
            )

        else:

            st.error("🔴 Prediction: Possible Leaf Spot Disease")

            st.write(
                "The leaf may show symptoms similar to leaf spot disease."
            )

            st.write(
                "Suggested action: Check the plant for spreading spots "
                "and maintain proper plant hygiene."
            )

        st.caption(
            "This is an educational prototype. "
            "The prediction is randomly generated and is not a "
            "professional agricultural diagnosis."
        )

else:

    st.warning("Please upload a leaf image to begin.")