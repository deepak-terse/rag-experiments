from langchain.vectorstores.chroma import Chroma
from utils.embeddings import get_embedding_function
from utils.config import get_root_directory

import os
import shutil

CHROMA_PATH = str(get_root_directory() / "chroma")

def get_database():
    return Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)