from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import getpass
import os

def load_llm():

    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    return ChatGoogleGenerativeAI(
        name='Gemini',
        model="gemini-1.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        verbose=True
    )
