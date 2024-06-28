# Simple Langchain Demo

A simple question answer app build with langchain


## Technologies Used

- Langchain: RAG framework
- PyPDF: Document Loader
- Chroma DB: Vector Storage
- Gradio: UI Library


## Prerequisites

- Python and PIP installed
- Ollama server: Download from https://ollama.com/


## Getting Started

1. Clone this code and navigate to 'simple-langchain' folder
2. Pull 'llama2' or any other model of your choice: `ollama pull llama2`
3. Run the ollama server by opening the app or from terminal: `ollama serve`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `python3 simple-langchain/src/app.py`. This will open the app at `http://127.0.0.1:7860` where you can find rest of the instructions

