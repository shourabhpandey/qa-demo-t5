# Modular NLP Question Answering System (T5 + FAISS + Sentence-BERT)

This project is a modular question answering system that can process large documents and structured tables using semantic search and a lightweight T5 model.

---

## Features

- Semantic retrieval using Sentence-BERT and FAISS for fast, relevant chunk search
- Supports long documents and tabular data inputs (CSV)
- Generates answers using a pretrained T5-small model
- Provides fallback answers ("No answer found") when confidence is low
- Simple interactive UI built with Streamlit
- Modular design for easy extension and adaptation to new domains

---

## Getting Started

### Prerequisites

Make sure you have Python 3.8+ installed.

### Installation

1. Clone the repo or download the source code.

2. Install the required dependencies:
```bash
pip install -r requirements.txt

## Running the Project

To run the command-line interface (CLI):

```bash
python main.py

streamlit run app.py

## Example Data

- `data/sample_doc.md` — Sample long document used for testing  
- `data/sample_table.csv` — Example table data for structured input

---

## Technologies Used

- [Sentence-BERT](https://www.sbert.net/) for semantic embeddings  
- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search  
- [HuggingFace Transformers](https://huggingface.co/transformers/) (`T5-small`)  
- [Streamlit](https://streamlit.io/) for UI

## Screenshot

Include a screenshot of your app UI here if available:

![QA App UI](screenshot.png)
