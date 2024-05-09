import gradio as gr
from scripts.query_data import query_data
from scripts.populate_database import populate_database
from utils.database import clear_database

def populate():
    logs = ""
    for value in populate_database():
        logs += value + '\n'
        yield logs

def clear():
    clear_database()
    return "Database cleared successfully"

def search(query_text):
    return query_data(query_text)

with gr.Blocks(title="Context Search App") as demo:
    gr.Markdown(
        """
        # Context Search AI

        ## Steps
        1. Install Ollama server and ensure that its running locally at http://localhost:11434 and llama2 model is installed. More details here - https://python.langchain.com/v0.1/docs/integrations/llms/ollama/
        2. Copy the pdf document you want to analyze to the 'data' folder and click on 'Populate Database'
        3. You can now began asking questions relevant to your document
        """)
    
    gr.Markdown(
        """
        ## Database Operations
        """)
        
    with gr.Column():
        with gr.Row():
            populate_btn = gr.Button("Populate Database", scale=1)
            clear_btn = gr.Button("Clear Database", scale=1)
        populate_output = gr.Textbox(label="Response", lines=3)

    gr.Markdown(
        """
        ## Search Database
        """)
    
    with gr.Row(equal_height=True):
        search_input = gr.Textbox(show_label=False, elem_id="", placeholder="Ask me anything about the shared document", scale=20)
        search_btn = gr.Button("Search", scale=1)

    search_output = gr.Textbox(label="Answer", lines=15, show_copy_button=True)

    populate_btn.click(fn=populate, outputs=populate_output, api_name="populate")
    clear_btn.click(fn=clear, outputs=populate_output, api_name="clear")
    search_btn.click(fn=search, inputs=search_input, outputs=search_output, api_name="search")

demo.launch()