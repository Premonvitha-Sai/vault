# 🔓 Private PDF Unlocker (Streamlit)

Decrypt password-protected PDFs locally. Files are processed in-memory; nothing is uploaded to third-party servers.

## ✨ Features
- 100% local processing (can be run offline).
- In-memory decryption using [`pypdf`](https://pypi.org/project/pypdf/).
- One-click download of the unlocked PDF.
- No file writes to disk by default.

## 🚀 Quick Start

```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the app
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## 🛡️ Privacy Notes
- This app uses only in-memory buffers for uploaded and processed PDFs.
- If you deploy publicly, ensure your hosting setup also respects privacy (e.g., behind a VPN or on your LAN).

## 🧩 Troubleshooting
- **Wrong password / unsupported encryption**: You'll see an error if the password is wrong or the encryption isn't supported by `pypdf`.
- **Large PDFs**: Increase `maxUploadSize` in `.streamlit/config.toml` if needed.
- **Run fully offline**: After installing dependencies once, you can run without internet access.

---
Made with ❤️ using Streamlit + pypdf.