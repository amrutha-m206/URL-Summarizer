import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Streamlit app configuration
st.set_page_config(page_title="Summarize Youtube Videos/Websites", page_icon="📜")
st.title("Summarize Youtube Videos/Websites 📜")
st.subheader("Summarize")

# Groq API and URL to be summarized
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

g_url = st.text_input("URL", label_visibility="collapsed")

# Validate Groq API key
if not groq_api_key.strip():
    st.warning("Please enter your Groq API key.")

# Validate URL
if not validators.url(g_url) and g_url.strip():
    st.error("Enter a valid URL.")

# Check if both API key and URL are provided
if st.button("Summarize the content from URL"):
    if not groq_api_key.strip():
        st.error("Please provide the Groq API key.")
    elif not validators.url(g_url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Processing..."):
                # Load the URL data
                if "youtube.com" in g_url:
                    loader = YoutubeLoader.from_youtube_url(g_url, add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[g_url],
                        ssl_verify=False,
                        header={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
                        },
                    )

                docs = loader.load()

                # Initialize Groq model
                llm = ChatGroq(model="Gemma-7b-It", groq_api_key=groq_api_key)

                # Define prompt template
                prompt_template = """
                Provide a summary of the following content in 300 words:
                Content={text}
                """
                prompt = PromptTemplate(
                    template=prompt_template, input_variables=["text"]
                )

                # Chain for summarization
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)

                st.success(output_summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
