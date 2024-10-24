import streamlit as st
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import os

# 1. Set up the app layout
st.title("CSV Data Analyzer with Google GenAI")

# Allow the user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# 2. Load CSV data with Pandas if the file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(df.head())  # Display the first few rows of the CSV

    # Provide an input box for the user to ask questions about the data
    user_question = st.text_input("Ask a question about the data:")

    # 3. If there's a question, process it using LangChain with Google GenAI
    if user_question:
        # Process the DataFrame if needed, depending on the question
        # Use LangChain to connect to Google GenAI
        genai.configure(api_key="AIzaSyDfx1l5gsXFb0ppiezCWdCXoEqw0eanm1A")
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

        # Construct a prompt that includes the data (e.g., summarize, filter)
        prompt = f"Here's the data: {df.to_string()}. Answer the following question: {user_question}"
        
        # Pass the prompt to the LLM and get the result
        st.write("prompt:", prompt)
        answer = llm.invoke(prompt)
        
        # 4. Display the answer to the user
        st.write("Answer:", answer)
