import streamlit as st
import pandas as pd
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import chromadb
import uuid
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
# Get GROQ API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Cold Email Generator", page_icon="📧")

st.title("📧 AI Cold Email Generator (RenderiQ)")
st.write("Generate customized cold emails from a job posting URL ✅")

#  Load Portfolio CSV ----
@st.cache_data
def load_portfolio():
    return pd.read_csv(r"C:\Users\Tanuja\Documents\cold-emails\my_portfolio.csv")

df = load_portfolio()

# ---- Initialize Vector DB ----
ef = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.PersistentClient("vectorstore")
collection = client.get_or_create_collection(name="portfolio", embedding_function=ef)

# Add portfolio to vector DB if empty
if collection.count() == 0:
    for _, row in df.iterrows():
        collection.add(
            documents=[row["Techstack"]],
            metadatas=[{"links": row["Links"]}],
            ids=[str(uuid.uuid4())]
        )

# ----  LLM Setup ----
llm = ChatGroq(
    temperature=0,
    groq_api_key=GROQ_API_KEY, 
    model_name="llama-3.3-70b-versatile"
)

# ---- STREAMLIT INPUT ----
url = st.text_input("🔗 Enter Job Posting URL")

if st.button("Generate Email ✨"):
    if url.strip() == "":
        st.error("❗ Please enter a valid URL")
    else:
        with st.spinner("⏳ Scraping job details..."):

            # ----  SCRAPE JOB ----
            loader = WebBaseLoader(url)
            pagedata = loader.load().pop().page_content

            # ---- Extract structured data ----
            prompt_extract = PromptTemplate.from_template("""
            ###SCRAPED TEXT FROM WEBSITE:
            {pagedata}

            ###INSTRUCTION:
            The scraped text is from a careers page.
            Extract job posting and return VALID JSON with ONLY:
            `role`, `experience`, `skills`, `description`.

            Empty values:
              - Text fields → ""
              - Skill list → []

            RETURN ONLY RAW VALID JSON (no text before/after).
            """)

            chain_extract = prompt_extract | llm
            res = chain_extract.invoke({"pagedata": pagedata})

            json_parser = JsonOutputParser()
            job = json_parser.parse(res.content)

        st.success("✅ Job Extracted")

        # ---- Query portfolio based on skills ----
        skill_list = job.get("skills", []) or []
        query_text = ",".join(skill_list) if skill_list else "Software, AI, Python"

        links = collection.query(
            query_texts=[query_text],
            n_results=3
        ).get("metadatas")

        # ---- Cold Email Prompt ----
        prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Mohan, a business development executive at RenderiQ.
        Write a cold email to the client about how RenderiQ can fulfill their needs.
        Add relevant portfolio links: {link_list}
        No preamble. Email only.

        ### EMAIL (NO PREAMBLE):
        """
        )

        chain_email = prompt_email | llm
        res_email = chain_email.invoke({"job_description": str(job), "link_list": links})

        st.subheader("📧 Generated Cold Email")
        st.write(res_email.content)

        st.success("✅ Done!")
