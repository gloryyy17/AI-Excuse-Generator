import streamlit as st
from transformers import pipeline, set_seed

# Load GPT-2 model
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

# Web UI
st.title("🤖 AI Excuse Generator")

context = st.text_input("Enter context (e.g., exam, meeting)")
reason = st.text_input("Enter reason (e.g., fever, power cut)")
urgency = st.selectbox("Urgency", ["low", "normal", "high"])

if st.button("Generate Excuse"):
    prompt = f"I couldn't attend the {context} because I had a {reason}. It was {urgency} level and"
    result = generator(prompt, max_length=50, num_return_sequences=1)
    excuse = result[0]['generated_text'].strip()
    st.success(f"🤖 Excuse:\n{excuse}")
st.write("Loading model... Please wait ⏳")
