import streamlit as st
import numpy as np
import pickle
from PIL import Image
import os

# =========================
# Load Model
# =========================
@st.cache_resource
def load_model():
    return pickle.load(open("rfc.pkl", "rb"))

rfc = load_model()

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Forest Cover Prediction",
    page_icon="🌲",
    layout="centered"
)

# =========================
# Title
# =========================
st.title("🌲 Forest Cover Type Prediction System")

# =========================
# Header Image
# =========================
try:
    header_img = Image.open("img.jpeg")
    st.image(
        header_img,
        caption="Forest Cover Prediction",
        use_container_width=True
    )
except:
    st.warning("Header image not found")

# =========================
# Feature Instructions
# =========================
st.subheader("Enter Feature Values")

st.write("Enter exactly 10 values in this order:")

st.code("""
1. Elevation
2. Horizontal_Distance_To_Roadways
3. Horizontal_Distance_To_Fire_Points
4. Wilderness_Area1
5. Wilderness_Area3
6. Wilderness_Area4
7. Soil_Type3
8. Soil_Type10
9. Soil_Type38
10. Soil_Type39
""")

# =========================
# User Input
# =========================
user_input = st.text_input(
    "Enter comma-separated values"
)

# =========================
# Cover Type Mapping
# =========================
cover_image_dict = {

    1: {
        "name": "Spruce/Fir",
        "image": "img_1.jpeg"
    },

    2: {
        "name": "Lodgepole Pine",
        "image": "img_2.jpeg"
    },

    3: {
        "name": "Ponderosa Pine",
        "image": "img_3.jpeg"
    },

    4: {
        "name": "Cottonwood/Willow",
        "image": "img_4.jpeg"
    },

    5: {
        "name": "Aspen",
        "image": "img_5.jpeg"
    },

    6: {
        "name": "Douglas-fir",
        "image": "img_6.jpeg"
    },

    7: {
        "name": "Krummholz",
        "image": "img_7.jpeg"
    }
}

# =========================
# Prediction Logic
# =========================
if user_input:

    try:

        # Convert input into list
        values = [
            x.strip()
            for x in user_input.split(',')
            if x.strip()
        ]

        # Validate feature count
        if len(values) != 10:

            st.error(
                "⚠️ Please enter exactly 10 values"
            )

        else:

            # Convert to numpy array
            features = np.array(
                [list(map(float, values))],
                dtype=np.float64
            )

            # Prediction
            prediction = int(
                rfc.predict(features)[0]
            )

            st.success(
                f"✅ Predicted Cover Type: {prediction}"
            )

            # Mapping
            info = cover_image_dict.get(prediction)

            if info:

                forest_name = info["name"]
                forest_image = info["image"]

                st.markdown("---")

                col1, col2 = st.columns([1, 2])

                # Forest Name
                with col1:
                    st.markdown(
                        f"## 🌳 {forest_name}"
                    )

                # Forest Image
                with col2:

                    if os.path.exists(forest_image):

                        img = Image.open(
                            forest_image
                        )

                        st.image(
                            img,
                            caption=forest_name,
                            use_container_width=True
                        )

                    else:
                        st.error(
                            "Image file not found"
                        )

            else:

                st.warning(
                    "No mapping found for this prediction"
                )

    except ValueError:

        st.error(
            "⚠️ Enter only numeric values separated by commas"
        )