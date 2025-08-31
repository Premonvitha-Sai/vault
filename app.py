import io
from typing import Optional

import streamlit as st
from pypdf import PdfReader, PdfWriter

st.set_page_config(page_title="Private PDF Unlocker", page_icon="🔓", layout="centered")

st.title("🔓 Private PDF Unlocker")
st.write(
    "Decrypt a password-protected PDF locally in your browser session. "
    "Your file is processed in-memory and is **not** uploaded to any third-party server."
)

with st.expander("Why is this private?"):
    st.markdown(
        "- Processing happens in your Streamlit app session; this script does not send files anywhere.\n"
        "- We use in-memory buffers (no disk writes).\n"
        "- You can run this app completely offline on your own machine."
    )

uploaded = st.file_uploader("Upload encrypted PDF", type=["pdf"])
password = st.text_input("PDF password", type="password")
col1, col2 = st.columns([1,1])

def decrypt_pdf(data: bytes, pwd: str) -> bytes:
    bio = io.BytesIO(data)
    reader = PdfReader(bio)
    if reader.is_encrypted:
        # pypdf returns 0/1/2 depending on success; raise if 0
        result = reader.decrypt(pwd)
        if result == 0:
            raise ValueError("Incorrect password or unsupported encryption.")
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    # Preserve metadata if present
    if reader.metadata:
        writer.add_metadata({k: v for k, v in reader.metadata.items() if isinstance(k, str)})
    out = io.BytesIO()
    writer.write(out)
    out.seek(0)
    return out.read()

with col1:
    unlock = st.button("Unlock PDF", type="primary", disabled=uploaded is None or len(password) == 0)
with col2:
    st.download_button(
        "Download Sample Encrypted PDF",
        data=b"",  # Placeholder; no sample provided
        file_name="",
        disabled=True,
        help="(No sample included — use your own encrypted PDF.)",
    )

if unlock:
    if uploaded is None:
        st.error("Please upload an encrypted PDF.")
    elif not password:
        st.error("Please enter the PDF password.")
    else:
        try:
            decrypted_bytes = decrypt_pdf(uploaded.read(), password)
            st.success("Success! Your PDF is unlocked. Click below to download.")
            st.download_button(
                label="⬇️ Download Unlocked PDF",
                data=decrypted_bytes,
                file_name=(uploaded.name.replace(".pdf", "") + "_unlocked.pdf") if uploaded.name else "unlocked.pdf",
                mime="application/pdf",
            )
        except Exception as e:
            st.error(f"Failed to unlock PDF: {e}")