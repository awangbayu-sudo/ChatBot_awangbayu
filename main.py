import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key dari .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOLE_API_KEY_AWANG_BAYU")

# Konfigurasi halaman
st.set_page_config(
    page_title="🎨 Chatbot Desain Grafis - Awang Bayu",
    page_icon="🎨",
    layout="centered",
)

# Sidebar Info
with st.sidebar:
    st.title("👨‍🎨 Tentang Awang Bayu")
    st.markdown("""
    - **Profesi**: Graphic Designer  
    - **Pengalaman**: 8+ tahun  
    - **Skill**: Photoshop, CorelDraw, Illustrator, PowerPoint, Canva, Figma  
    - **Project**: 400+  
    - **Client**: 200+ dalam & luar negeri  
    - **Rate**: $25/jam (negotiable)  
    - 🌐 [Portofolio](https://awangbayu.com)  
    """)

# Judul utama
st.title("🎨 Chatbot Desain Grafis - Awang Bayu")
st.caption("Tanyakan apa saja tentang desain grafis, branding, presentasi, atau UI/UX.")

# Input chat user
user_input = st.chat_input("Ketik pertanyaan di sini...")

# Placeholder area chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan riwayat percakapan
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)

# Jika ada input user
if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Default jawaban (fallback jika API tidak jalan)
    ai_answer = "Saya sedang memproses pertanyaan Anda. Jika AI tidak aktif, silakan cek portofolio saya di [awangbayu.com](https://awangbayu.com)."

    # Jika ada API key, coba hubungkan dengan Gemini
    if GOOGLE_API_KEY:
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            if response and response.text:
                ai_answer = response.text
        except Exception as e:
            ai_answer = f"⚠️ Gagal menghubungkan AI: {e}"

    # Simpan jawaban ke riwayat
    st.session_state.messages.append(("assistant", ai_answer))
    with st.chat_message("assistant"):
        st.markdown(ai_answer)
