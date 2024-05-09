from langchain.schema.document import Document
from utils.document import load_documents, split_documents
from utils.database import get_database, clear_database

def populate_database():
    documents = load_documents()
    chunks = split_documents(documents)
    return add_to_database(chunks)

# Add chunks to database
def add_to_database(chunks: list[Document]):
    db = get_database()

    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    yield f"Number of existing documents in DB: {len(existing_ids)}"

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        yield f"👉 Adding new documents: {len(new_chunks)}"
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        yield "New documents added successfully"
        db.persist()
    else:
        yield "✅ No new documents to add"

# Returns chunks with newly created ids attached which looks like "monopoly.pdf:6:2" - Page Source: Page Number: Chunk Index
def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source").rsplit('/',1)[-1]
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the chunk metadata.
        chunk.metadata["id"] = chunk_id

    return chunks
