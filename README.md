<div align="center">

# 📄 RAG Based PDF Reader

### 🚀 Retrieval-Augmented Generation (RAG) Application for Intelligent PDF Question Answering

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A67E?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-6C63FF?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge)

An AI-powered application that enables users to upload PDF documents and ask natural language questions using **Retrieval-Augmented Generation (RAG)**.

</div>

---

# 📌 Project Overview

RAG Based PDF Reader is an AI-powered document question-answering application built using **LangChain**, **ChromaDB**, **Hugging Face Embeddings**, and **Ollama**.

Instead of relying only on an LLM's knowledge, the application retrieves the most relevant information directly from uploaded PDF documents, ensuring more accurate and context-aware responses.

---

# ✨ Features

- 📄 Upload PDF documents
- 📚 Extract text from PDFs
- ✂️ Automatic text chunking
- 🧠 Generate embeddings using Hugging Face
- 🗂 Store embeddings in ChromaDB
- 🔍 Semantic similarity search
- 🤖 Answer questions using Ollama LLM
- 💬 Natural language querying
- ⚡ Fast retrieval pipeline
- 🎯 Context-aware responses
- 🌐 Simple Streamlit interface

---

# 🏗️ Architecture Diagram

```text
                  +--------------------+
                  |    Upload PDF      |
                  +---------+----------+
                            |
                            ▼
                 +----------------------+
                 |   PDF Text Extractor |
                 +----------+-----------+
                            |
                            ▼
              +----------------------------+
              | Recursive Text Splitter    |
              +-------------+--------------+
                            |
                            ▼
              +----------------------------+
              | HuggingFace Embeddings     |
              +-------------+--------------+
                            |
                            ▼
                +-------------------------+
                |      Chroma Vector DB   |
                +-------------+-----------+
                              |
                    Similarity Search
                              |
                              ▼
                +--------------------------+
                |   Relevant Context       |
                +-------------+------------+
                              |
                              ▼
                  +-----------------------+
                  |     Ollama LLM        |
                  +-----------+-----------+
                              |
                              ▼
                    💬 Generated Answer
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | RAG Pipeline |
| ChromaDB | Vector Database |
| Hugging Face | Embeddings |
| Ollama | Local LLM |
| PyPDFLoader | PDF Processing |

---

# 📂 Folder Structure

```text
RAG_Based_PDF_Reader
│
├── data/
│   └── sample.pdf
│
├── utils/
│
├── app.py
├── ingest.py
├── rag.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/krithan-an/RAG_Based_PDF_Reader.git

cd RAG_Based_PDF_Reader
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download from

https://ollama.com

Pull a model

```bash
ollama pull llama3
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 💻 Demo

## Home Screen


(Add screensh<img width="959" height="485" alt="Screenshot 2026-07-16 080359" src="https://github.com/user-attachments/assets/53313681-b66a-4829-a5e6-de5a7dce82e9" />


## Ask Questions


<img width="958" height="497" alt="Screenshot 2026-07-16 080306" src="https://github.com/user-attachments/assets/951c0896-e04c-46c7-a9d2-4b71fe0f7c70" />


# 📈 Future Enhancements

- ✅ Multiple PDF Upload Support
- ✅ Chat History
- ✅ Conversation Memory
- ✅ OCR Support for Scanned PDFs
- ✅ Source Citation
- ✅ Multi-user Authentication
- ✅ Cloud Deployment
- ✅ PDF Summarization
- ✅ Voice-based Queries
- ✅ Support for DOCX and TXT files

---

# 🚀 Use Cases

- Research Paper Analysis
- Company Documentation
- Legal Document Search
- Educational Learning
- Technical Documentation
- Internal Knowledge Base
- Policy Document Assistant

---

GitHub: https://github.com/krithan-an

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

and feel free to contribute!




