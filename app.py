import streamlit as st
from retriever import Retriever
from answerer import Answerer
from table_utils import table_to_text

st.title("Mini QA Demo")

question = st.text_input("Ask a question:")

if question:
    with open("data/sample_doc.md", "r") as f:
        doc_text = f.read()

    table_text = table_to_text("data/sample_table.csv")

    retriever = Retriever()
    retriever.add_text(doc_text)
    retriever.add_text(table_text)

    top_chunks = retriever.retrieve(question)
    context = " ".join(top_chunks)

    answerer = Answerer()
    answer = answerer.generate_answer(context, question)

    st.subheader("Top Context:")
    st.write(context)

    st.subheader("Answer:")
    st.success(answer)
