import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer


def main():

    # Set up Streamlit interface
    st.set_page_config(
        page_title="Interactive Visualization Tool", page_icon="📈", layout="wide"
    )

    st.header("📈 Interactive Visualization Tool")
    st.caption("### This tool help you visialize your data.")
    with st.sidebar:
        st.html("""
                <div>
                Developed by <span style="color:blue">DXA</span>
                </div>
                """)
    # Render pygwalker
    if st.session_state.get("df") is not None:
        pyg_app = StreamlitRenderer(st.session_state.df)
        pyg_app.explorer()

    else:
        st.info("Please upload a dataset to begin using the interactive visualization tools")


if __name__ == "__main__":
    main()