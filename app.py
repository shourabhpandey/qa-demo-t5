import streamlit as st
from retriever import Retriever
from answerer import Answerer
from table_utils import table_to_text

st.set_page_config(page_title="QA Demo", layout="wide")

# ---------- Title Section ----------
st.markdown(
    """
    <div style='text-align: center;'>
        <h3 style='margin-bottom: 5px;'>💬 Smart QA System</h3>
        <p style='font-size: 14px; color: #666;'>Ask questions from documents, tables, or your own text using T5 + semantic search</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr style='margin: 15px 0;'>", unsafe_allow_html=True)

# ---------- Section: Ask from Sample Document ----------
st.markdown("<h5 style='color: #333;'>📚 Ask from Sample Data</h5>", unsafe_allow_html=True)

with st.form("sample_form"):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        question = st.text_input("", placeholder="e.g., What is the summary of the document?")
        submitted = st.form_submit_button("Get Answer")

    if submitted and question:
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

        with col2:
            st.markdown("<small style='color: #666;'>🔍 Top Context</small>", unsafe_allow_html=True)
            st.code(context[:800] + ("..." if len(context) > 800 else ""))

            st.markdown("<small style='color: #666;'>✅ Answer</small>", unsafe_allow_html=True)
            st.success(answer)

# ---------- Divider ----------
st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

# ---------- Section: Ask from Custom Text ----------
st.markdown("<h5 style='color: #333;'>📝 Ask from Your Own Text</h5>", unsafe_allow_html=True)

with st.form("custom_form"):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        custom_text = st.text_area("Paste your text below:", height=150, placeholder="Paste your article or content here...")
        custom_question = st.text_input("Your Question", placeholder="e.g., What are the key takeaways?")
        custom_submitted = st.form_submit_button("Get Answer")

    if custom_submitted and custom_text and custom_question:
        retriever = Retriever()
        retriever.add_text(custom_text)

        top_chunks = retriever.retrieve(custom_question)
        context = " ".join(top_chunks)

        answerer = Answerer()
        answer = answerer.generate_answer(context, custom_question)

        with col2:
            st.markdown("<small style='color: #666;'>🔍 Top Context</small>", unsafe_allow_html=True)
            st.code(context[:800] + ("..." if len(context) > 800 else ""))

            st.markdown("<small style='color: #666;'>✅ Answer</small>", unsafe_allow_html=True)
            st.success(answer)
