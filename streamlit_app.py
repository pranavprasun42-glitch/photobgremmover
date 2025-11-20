import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Photo Background Remover", page_icon="✨")

st.title("🔥 PHOTO BACKGROUND REMOVER")
st.write("Upload any image → get transparent background instantly • Free & Unlimited")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "webp"])

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    original = Image.open(uploaded_file)
    with col1:
        st.image(original, caption="Original", use_column_width=True)

    with st.spinner("Removing background... (takes 3-8 seconds)"):
        input_bytes = uploaded_file.getvalue()
        output_bytes = remove(input_bytes)
    result = Image.open(io.BytesIO(output_bytes))

    with col2:
        st.image(result, caption="Background Removed ✨", use_column_width=True)

    buf = io.BytesIO()
    result.save(buf, format="PNG")
    st.download_button(
        label="📥 Download Transparent PNG",
        data=buf.getvalue(),
        file_name="no-background.png",
        mime="image/png"
    )
