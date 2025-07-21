=========================================
  AI Excuse Generator – README
=========================================

Project Title:
---------------
AI-Based Excuse Generator using GPT-2 and Streamlit


Overview:
----------
This project is a simple AI-powered web application that generates believable and personalized excuses based on user inputs like context (e.g., "school exam"), reason (e.g., "fever"), and urgency level (low/normal/high).

It uses the GPT-2 language model from Hugging Face Transformers and is built using the Streamlit web framework in Python.


How to Run the Project:
------------------------

Step 1: Make sure you have Python 3.10 or 3.11 installed.
         (Python 3.13 is not supported by PyTorch)

Step 2: Open a terminal in the project folder and install the required packages:

    pip install -r requirements.txt

Step 3: Run the app with:

    streamlit run excuse_app.py

Step 4: The app will open in your browser at:

    http://localhost:8501

Step 5: Enter your context, reason, and urgency, and click “Generate Excuse” to get an AI-generated excuse.

    
Features:
----------
✓ GPT-2 based excuse generation  
✓ Simple and user-friendly web interface  
✓ Handles custom inputs  
✓ Runs completely offline after first download


Requirements:
--------------
- Python 3.10 or 3.11
- streamlit
- transformers
- torch

(Already listed in `requirements.txt`)


Credits:
---------
Developed by: Glory Jagjivan  
Language model: GPT-2 by Hugging Face  
Frontend: Streamlit


Optional Add-ons:
------------------
- Save excuses to history
- Generate fake medical PDFs
- Deploy online via Streamlit Cloud

