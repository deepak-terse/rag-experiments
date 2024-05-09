from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    # Ensure that you've ollama server running at the specified url and with specified model
    return OllamaEmbeddings(
        model="llama2", 
        base_url="http://localhost:11434"
    )