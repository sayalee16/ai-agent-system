# Multi-Agent AI System

A modular, intelligent system that classifies and processes various document formats—**PDF**, **JSON**, and **Email**—using specialized agents. Built with Streamlit and LLMs, the system uses a central **Classifier Agent** and routes inputs to **format-specific agents**, while maintaining shared context in a **SQLite memory module**.

##  Features

- **Classifier Agent**  
   Detects format (PDF, JSON, Email) and intent (Invoice, RFQ, Complaint, etc.)

- **Email Agent**  
   Extracts sender, urgency, intent from plain email text

- **JSON Agent**  
   Parses structured JSON, reformats to target schema

- **PDF Agent**  
   Extracts raw text from PDFs 

- **Shared Memory (SQLite)**  
   Logs all activity with timestamps, formats, intents, and extracted data

##  Tech Stack

- Python
- Streamlit
- Langchain / Gemini / OpenAI (LLM based classification)
- SQLite (shared memory)

