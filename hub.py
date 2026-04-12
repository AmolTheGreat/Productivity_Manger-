import streamlit as st

# 1. This makes the browser tab look cool
st.set_page_config(page_title="Guardian AI Hub", page_icon="🛡️", layout="centered")

# 2. Main Title and Intro
st.title("🛡️ AMOL GIRI: GUARDIAN AI")
st.markdown("### *Stay Focused. Stay Productive.*")
st.write("This tool helps you stay off distracting sites while you're working on your big projects.")

st.divider()

# 3. The Logic to find your file
try:
    with open("enforcer.exe", "rb") as file:
        st.download_button(
            label="🚀 DOWNLOAD GUARDIAN AI (EXE VERSION)",
            data=file,
            file_name="GuardianAI.exe",
            mime="application/octet-stream"
        )
    st.success("✅ The 'One-Click' version is ready! No Python installation needed.")
    
    st.info("💡 **Instructions:** After downloading, just double-click 'GuardianAI.exe' to launch. "
            "If Windows shows a 'Protected your PC' warning, click **More Info** then **Run Anyway**.")

except FileNotFoundError:
    st.error("❌ FILE ERROR: I can't find 'enforcer.exe' in your GitHub folder.")
    st.write("Double-check that the name is spelled exactly `enforcer.exe` on GitHub!")

# 4. Footer
st.divider()
st.caption("Developed by Amol Giri | WAVE Magnet Program 2026")