from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import ollama

# -----------------------------------------
# Load Embedding Model
# -----------------------------------------
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------------------
# Load Chroma Vector Database
# -----------------------------------------
db = Chroma(
    persist_directory="db",
    embedding_function=embedding
)

# -----------------------------------------
# Function to Ask Questions
# -----------------------------------------
def ask_question(question):
    try:
        # Retrieve top 6 relevant chunks using MMR
        docs = db.max_marginal_relevance_search(
            question,
            k=6,
            fetch_k=12
        )

        if not docs:
            return "No relevant information found in the document."

        # -----------------------------
        # Debug: Print Retrieved Chunks
        # -----------------------------
        print("\n" + "=" * 80)
        print("Retrieved Chunks")
        print("=" * 80)

        for i, doc in enumerate(docs, 1):
            print(f"\nChunk {i}")
            print("-" * 60)
            print(doc.page_content[:500])

        # Combine all retrieved chunks
        context = "\n\n".join(doc.page_content for doc in docs)

        # Better Prompt
        prompt = f"""
You are an intelligent AI assistant.

Your task is to answer ONLY using the information provided in the context.

Rules:
1. Read the entire context carefully.
2. Give a complete and detailed answer.
3. If information is spread across multiple sections, combine it.
4. Do NOT make up information.
5. If the answer is not found in the context, reply:
"I couldn't find that information in the document."

---------------- CONTEXT ----------------
{context}
-----------------------------------------

Question:
{question}

Answer:
"""

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"


# -----------------------------------------
# Command Line Chat
# -----------------------------------------
if __name__ == "__main__":

    print("=" * 60)
    print("        RAG CHATBOT USING OLLAMA")
    print("=" * 60)
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            print("Please enter a question.\n")
            continue

        answer = ask_question(question)

        print("\nBot:\n")
        print(answer)
        print("\n" + "-" * 70)