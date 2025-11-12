# email-generator
# Cold Email Generator 🤖✉️

A Python-based project that generates personalized cold emails for job applications using Jupyter Notebook. It extracts job information from postings and combines it with portfolio data to create professional, tailored emails.

---

## 🔹 Features

- Generate personalized cold emails for any job posting.
- Extract key information from job descriptions automatically.
- Integrates portfolio links for added personalization.
- Easy-to-use interface through Jupyter Notebook.

---

## 🏗️ Technical Architecture

The project uses **LLMs (Llama 3.1)** and **Chromadb** to process job postings and generate emails:

1. **Job Posting Extraction**
   - Extract text from career pages using Python.
   - Convert the job information into structured data:

```python
job = {
  'role': 'Senior Software Engineer',
  'skills': ['2 years experience in React'],
  'description': 'We are looking for a...'
}
