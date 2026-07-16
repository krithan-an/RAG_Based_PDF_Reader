import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ---------------------------------------
# Delete old database (optional)
# ---------------------------------------
if os.path.exists("db"):
    shutil.rmtree("db")
    print("Old Chroma database deleted.")

# ---------------------------------------
# Load PDF
# ---------------------------------------
loader = PyPDFLoader("data/sample.pdf")
documents = loader.load()

print(f"Loaded {len(documents)} pages.")

# ---------------------------------------
# Split into chunks
# ---------------------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

# Add page numbers as metadata
for chunk in chunks:
    if "page" not in chunk.metadata:
        chunk.metadata["page"] = "Unknown"

print(f"Created {len(chunks)} chunks.")

# ---------------------------------------
# Embedding Model
# ---------------------------------------
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------------------
# Create Chroma Database
# ---------------------------------------
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="db"
)

print("\nVector Database Created Successfully!")
print(f"Stored {len(chunks)} chunks in ChromaDB.")