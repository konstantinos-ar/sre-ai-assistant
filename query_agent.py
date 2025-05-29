from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def get_retrieval_chain(vector_store):
    llm = ChatOpenAI(model="gpt-4")
    retriever = vector_store.as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

def query_ai(prompt: str, chain):
    return chain.run(prompt)