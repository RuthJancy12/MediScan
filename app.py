import streamlit as st
import easyocr
import cv2
import numpy as np
from medicine_info import search_medicine


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MediScan",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# DARK BACKGROUND ONLY
# ============================================================

st.markdown("""
<style>

    /* Main dark background */
    .stApp {
        background-color: #111827;
    }

    /* Main content */
    .block-container {
        max-width: 1100px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    /* Text */
    .stApp p,
    .stApp label,
    .stMarkdown {
        color: #e5e7eb;
    }

    /* Headings */
    h1, h2, h3 {
        color: #f3f4f6 !important;
    }

    /* Upload area */
    [data-testid="stFileUploader"] {
        background-color: #1f2937;
        border-radius: 12px;
        padding: 10px;
    }

    /* Hide Streamlit menu */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.title("💊 MediScan")

st.markdown(
    "### Smart Medicine Label Reader"
)

st.write(
    "Upload a medicine label image to extract text "
    "and find general label information."
)


# ============================================================
# INFORMATION
# ============================================================

st.info(
    "MediScan provides general label information for "
    "demonstration purposes. It does not provide dosage "
    "or personalized medical advice."
)


# ============================================================
# LOAD EASY OCR
# ============================================================

@st.cache_resource
def load_reader():

    return easyocr.Reader(["en"])


reader = load_reader()


# ============================================================
# IMAGE UPLOAD
# ============================================================

st.subheader("📷 Upload a Medicine Label")

uploaded_file = st.file_uploader(
    "Choose a medicine image",
    type=["jpg", "jpeg", "png"]
)


# ============================================================
# PROCESS IMAGE
# ============================================================

if uploaded_file is not None:

    # --------------------------------------------------------
    # Convert uploaded file to image
    # --------------------------------------------------------

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )


    # --------------------------------------------------------
    # Check image
    # --------------------------------------------------------

    if image is None:

        st.error(
            "❌ Could not read the uploaded image."
        )

    else:

        # ====================================================
        # SHOW IMAGE
        # ====================================================

        st.subheader("🖼️ Uploaded Image")

        st.image(
            cv2.cvtColor(
                image,
                cv2.COLOR_BGR2RGB
            ),
            use_container_width=True
        )


        # ====================================================
        # OCR
        # ====================================================

        with st.spinner(
            "🔍 Reading medicine label..."
        ):

            results = reader.readtext(image)


        # ====================================================
        # EXTRACT TEXT
        # ====================================================

        extracted_text = []

        for result in results:

            text = result[1]

            extracted_text.append(text)


        # ====================================================
        # SHOW EXTRACTED TEXT
        # ====================================================

        st.subheader("🔍 Extracted Text")


        if extracted_text:

            for text in extracted_text:

                st.write(text)


            # =================================================
            # DETECT MEDICINE NAME
            # =================================================

            medicine_name = extracted_text[0].strip()


            st.markdown(
                f"### 💊 Detected Medicine: "
                f"**{medicine_name}**"
            )


            # =================================================
            # SEARCH DATASET
            # =================================================

            medicine = search_medicine(
                medicine_name
            )


            # =================================================
            # MEDICINE FOUND
            # =================================================

            if medicine is not None:

                st.subheader(
                    "💊 Medicine Information"
                )


                st.success(
                    "✓ Medicine found in project dataset"
                )


                # ------------------------------------------------
                # INFORMATION
                # ------------------------------------------------

                col1, col2 = st.columns(2)


                with col1:

                    st.markdown(
                        f"""
                        **Medicine Name**

                        {medicine["product_name"]}
                        """
                    )

                    st.markdown(
                        f"""
                        **Strength**

                        {medicine["strength"]}
                        """
                    )

                    st.markdown(
                        f"""
                        **Manufacturer**

                        {medicine["manufacturer"]}
                        """
                    )


                with col2:

                    st.markdown(
                        f"""
                        **Active Ingredient**

                        {medicine["active_or_main_ingredient"]}
                        """
                    )

                    st.markdown(
                        f"""
                        **Form**

                        {medicine["dosage_or_form"]}
                        """
                    )

                    st.markdown(
                        f"""
                        **Common Use**

                        {medicine["common_use"]}
                        """
                    )


            # =================================================
            # MEDICINE NOT FOUND
            # =================================================

            else:

                st.warning(
                    f"⚠️ '{medicine_name}' "
                    "was not found in the dataset."
                )


        # ====================================================
        # NO TEXT FOUND
        # ====================================================

        else:

            st.warning(
                "⚠️ No readable text was detected "
                "in the image."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "MediScan • AI & Data Science Project • "
    "Python + EasyOCR + OpenCV + Streamlit"
)