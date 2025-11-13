# 🚀 Cold Email Generator 🤖✉️  
**Smartly generate personalized cold emails for job applications using AI**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)
![LLM](https://img.shields.io/badge/Model-Llama_3.1-purple)
![Database](https://img.shields.io/badge/VectorDB-ChromaDB-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🧠 Overview

The **Cold Email Generator** is a Python-based project designed to help professionals or students create personalized, professional-grade cold emails for job applications.  
It extracts job information directly from career pages, processes it using **LLMs (Llama 3.1)**, and combines it with your portfolio details stored in **Chromadb** — generating perfectly tailored emails in seconds.

---

## ✨ Features

- 🔍 **Automatic Job Description Extraction** – Extracts text directly from career or job pages.  
- 🤖 **AI-Powered Email Generation** – Uses **Llama 3.1** to write customized cold emails.  
- 💼 **Portfolio Integration** – Includes relevant portfolio/project links via **Chromadb**.  
- 🧱 **Modular & Extensible** – Easily modify prompts or integrate new AI models.  
- 💡 **Simple to Use** – Run it directly in Jupyter Notebook.

---

## 🏗️ Technical Architecture

Below is the **architecture diagram** representing the core workflow:  

<p align="center">
  <img src="1dfa0192-7021-4789-9693-68e13d66bc9e.png" alt="Cold Email Generator Architecture" width="700"/>
</p>

### 🔹 Workflow

1. **Extract Text from Career Page**  
   → The system extracts raw job descriptions from company websites.

2. **Process using LLM (Llama 3.1)**  
   → The extracted text is parsed into structured job information:
   ```python
   job = {
     'role': 'Senior Software Engineer',
     'skills': ['2 years experience in React'],
     'description': 'We are looking for a...'
   }
