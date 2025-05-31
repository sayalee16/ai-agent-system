import fitz  

def process_pdf(content):
        # Open PDF and extract text
        doc = fitz.open(stream=content, filetype="pdf")
        text = ""
        
        # Get text from each page
        for page in doc:
            text += page.get_text() + "\n"
        
        doc.close()
        return {"text": text.strip() or "No text found"}
        