import streamlit as st
import qrcode
from PIL import Image
import io

st.title("QR Code Generator")

data = st.text_input("Enter the data to encode in the QR code:")

if st.button("Generate QR Code"):
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert PIL image to bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        st.image(img_bytes, caption="Generated QR Code", use_column_width=True)
        st.success("QR Code generated and displayed.")
    else:
        st.error("Please enter some data to generate a QR code.")
