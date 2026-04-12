import streamlit as st
import os

st.set_page_config(page_title="Guardian AI Debugger", page_icon="🔍")
st.title("🛡️ AMOL GIRI: GUARDIAN AI")

# --- THE DETECTIVE WORK ---
folder_name = "CODING CLASS"
file_name = "enforcer.pyw"
full_path = os.path.join(folder_name, file_name)

st.subheader("System Diagnostic")

# 1. Check if the folder even exists
if not os.path.exists(folder_name):
    st.error(f"❌ ERROR: I don't see a folder named '{folder_name}'.")
    st.write("Folders I DO see:", os.listdir("."))
    
# 2. If folder exists, check if the file is inside it
elif not os.path.exists(full_path):
    st.error(f"❌ ERROR: Found '{folder_name}', but '{file_name}' is NOT inside it.")
    st.write(f"Files inside '{folder_name}':", os.listdir(folder_name))

# 3. If everything is perfect, show the button
else:
    st.success("✅ SYSTEM READY: Guardian AI located!")
    with open(full_path, "rb") as file:
        st.download_button(
            label="🚀 DOWNLOAD & LAUNCH GUARDIAN AI",
            data=file,
            file_name="GuardianAI.pyw",
            mime="text/x-python"
        )

st.divider()
st.caption("Amol's Focus Enforcer v16.2 | Debug Mode")