from .loader import load_pdf
from .splitter import split_documents
from .embedder import get_embedding_model
from .vectorstore import create_vector_store

def ingest_pdf(file_path: str):

    # 1. Load
    documents = load_pdf(file_path)

    print('File Loaded')

    # 2. Chunk
    chunks = split_documents(documents)

    print("Chunks Made")

    # 3. Embeddings
    embeddings = get_embedding_model()

    print("Embeddings Made")

    # 4. Store
    vectordb = create_vector_store(chunks, embeddings)

    print(f"Ingested {len(chunks)} chunks successfully.")

    return vectordb