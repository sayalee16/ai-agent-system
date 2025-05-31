import streamlit as st
from agents.classifier import classify_input
from agents.email_classifer import process_email
from agents.json_classifer import process_json
from agents.pdf_classifer import process_pdf
from memory.memory import log_to_memory, fetch_logs

st.set_page_config(page_title="Multi-Agent AI System", layout="centered")
st.title("Multi-Agent AI System")
st.markdown("Classify & extract insights from PDF, JSON, or Email using intelligent agents.")

input_type = st.selectbox("Select Input Format", ["PDF", "JSON", "Email"])

uploaded_file = None
email_text = None

if input_type == "Email":
    email_text = st.text_area("Paste your email content here", height=200)
else:
    uploaded_file = st.file_uploader("Upload your file", type=["pdf", "json"])

if st.button("Classify and Process"):
    if input_type == "Email":
        if not email_text:
            st.error("Please enter the email content.")
        else:
            fmt, intent = classify_input(email_text)
            st.write(f"Format: {fmt}, Intent: {intent}")
            result = process_email(email_text)
            log_to_memory("email", fmt, intent, result.get("sender", ""), result)
            st.success("Email processed successfully!")
            st.write(result)

    elif input_type == "JSON":
        if not uploaded_file:
            st.error("Please upload a JSON file.")
        else:
            content = uploaded_file.read().decode("utf-8")
            fmt, intent = classify_input(content)
            st.write(f"Format: {fmt}, Intent: {intent}")
            result = process_json(content)
            log_to_memory("json", fmt, intent, None, result)
            st.success("JSON processed successfully!")
            st.write(result)

    elif input_type == "PDF":
        if not uploaded_file:
            st.error("Please upload a PDF file.")
        else:
            content = uploaded_file.read()
            fmt, intent = classify_input(content)
            st.write(f"Format: {fmt}, Intent: {intent}")
            result = process_pdf(content)
            log_to_memory("pdf", fmt, intent, None, result)
            st.success("PDF processed successfully!")
            st.write(result)

with st.sidebar:
    st.header("📜 Memory Logs")
    if st.button("Show Logs"):
        logs = fetch_logs(15)  # You can adjust limit
        if logs:
            for log in logs:
                st.markdown(f"""
                    **ID**: {log[0]}  
                    **Type**: {log[1]}  
                    **Format**: {log[2]}  
                    **Intent**: {log[3]}  
                    **Time**: {log[4]}  
                    **Sender**: {log[5]}  
                    **Result**:  
                    ```json
{log[6]}
                    ```
                    ---
                """)
        else:
            st.info("No logs found yet.")
