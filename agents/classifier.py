import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)  
model = genai.GenerativeModel("gemini-2.0-flash") 

def classify_input(input_text):
    prompt = f"""
            Classify the following content:
            1. Format: [pdf, email, json]
            2. Intent: [Invoice, RFQ, Complaint, Regulation, General Inquiry]

            Reply exactly like this (no code blocks, no JSON):
            Format: ...
            Intent: ...
            Content:{input_text}
  """

    response = model.generate_content(prompt)
    if response and response.text:
        lines = response.text.strip().splitlines()
        if len(lines) >= 2 and "Format:" in lines[0] and "Intent:" in lines[1]:
            fmt = lines[0].split(":", 1)[1].strip().lower()
            intent = lines[1].split(":", 1)[1].strip()
            return fmt, intent
        else:
            return "unknown", "unknown"
    else:
        return "unknown", "unknown"

# text = "Subject: Invoice for April\nPlease find the invoice attached."
# fmt, intent = classify_input(text)
# print(fmt, intent)

