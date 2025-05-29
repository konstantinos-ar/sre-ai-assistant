from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def build_index(documents: list[str]):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.create_documents(documents)
    vector_store = FAISS.from_documents(chunks, OpenAIEmbeddings())
    return vector_store
