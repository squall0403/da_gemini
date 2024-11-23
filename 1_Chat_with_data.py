import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent

from src.models.llms import load_llm
from src.ultis import execute_plt_code

load_dotenv()

def process_query(da_agent, query):
    response = da_agent.invoke({"input": query})

    # 4. Display the answer to the user
    st.write("Answer:" + "\n")
    action = response["output"]

    if "plot" in action:
        st.write(action)

        fig = execute_plt_code(action.replace('```python','').replace('```',''), df=st.session_state.df)
        if fig:
            st.pyplot(fig)

        st.write("**Executed code:**")
        st.code(action)

    else:
        st.write(action)

def main():
    # 1. Set up the app layout
    # Set up streamlit interface
    st.set_page_config(page_title="AI Data Analysis Tool", page_icon="📊", layout="centered")
    st.header("📊 AI Data Analysis Tool")
    st.caption(
        "### This uses AI to assist your daily data analysis tasks."
    )

    # Allow the user to upload a CSV file
    with st.sidebar:
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        st.html("""
                <div>
                Developed by <span style="color:blue">DXA</span>
                </div>
                """)

     # Load llms model
    llm = load_llm() 

    if uploaded_file is not None:
     st.session_state.df = pd.read_csv(uploaded_file)
     st.write("Data Preview:")
     st.write(st.session_state.df.head())  # Display the first few rows of the CSV

     # Provide an input box for the user to ask questions about the data
     user_question = st.text_input("Ask a question about the data:")

     if user_question:
       # Process the DataFrame if needed, depending on the question
       # Use LangChain to connect to Google GenAI

       # Construct a prompt that includes the data (e.g., summarize, filter)
       prompt = f"Here's the data: {st.session_state.df.to_string()}. Answer the following question: {user_question}"
       
       da_agent = create_pandas_dataframe_agent(
            llm=llm,
            df=st.session_state.df,
            agent_type="tool-calling",
            allow_dangerous_code=True,
            verbose=True,
            return_intermediate_steps=True,
        )
       with st.spinner("Processing..."):
        process_query(da_agent, prompt)

        # Display chat history

if __name__ == "__main__":
    main()
