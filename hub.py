import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Guardian AI Hub", page_icon="🛡️")

# 2. Title and Info
st.title("🛡️ AMOL GIRI: GUARDIAN AI")
st.subheader("Zero-Tolerance Focus Enforcer")

st.markdown("""
This tool automatically detects and closes distracting apps like **Roblox, YouTube, and TikTok** to help you stay focused on your **Math and Coding** goals.
""")

st.info("SYSTEM STATUS: ONLINE (v16.2)")

# 3. The Download Button (Looking inside your folder)
try:
    # This looks inside 'CODING CLASS' for your script
    with open("CODING CLASS/enforcer.pyw", "rb") as file:
        st.download_button(
            label="🚀 DOWNLOAD & LAUNCH GUARDIAN AI",
            data=file,
            file_name="GuardianAI.pyw",
            mime="text/x-python"
        )
    st.success("File found in 'CODING CLASS'! Ready for download.")
except FileNotFoundError:
    st.error("Still can't find 'enforcer.pyw'. Check if 'CODING CLASS' is spelled exactly like that on GitHub!")

# 4. Footer
st.divider()
st.caption("Developed by Amol | Master of Python | WAVE Magnet Student")