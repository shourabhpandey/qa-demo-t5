## 🔗 Live Demo

👉 [Click here to try the app](https://app-demo-t5.streamlit.app)

No setup needed — runs directly in your browser.


# Modular NLP Question Answering System

A modular question answering system that processes large documents and structured tables using semantic search (Sentence-BERT + FAISS) and a lightweight T5 model for generating accurate answers.

---

## Features

- **Semantic Retrieval**: Uses Sentence-BERT for semantic embeddings and FAISS for fast, relevant chunk search.
- **Multi-Format Input**: Supports long documents and tabular data (CSV) as input sources.
- **Answer Generation**: Leverages a pretrained T5-small model from HuggingFace for generating concise answers.
- **Fallback Mechanism**: Provides "No answer found" when confidence scores are low.
- **Interactive UI**: Includes a simple, user-friendly interface built with Streamlit.
- **Modular Design**: Easily extensible for new domains or custom use cases.

---

## Getting Started

### Prerequisites

- **Python**: Version 3.8 or higher.
- **Git**: For cloning the repository.
- A compatible environment (e.g., virtualenv, conda) is recommended.

### Installation

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

- **Command-Line Interface (CLI)**:
  Run the main script to use the system via the terminal:
  ```bash
   python main.py
   ```

- **Interactive Web UI**:
  Launch the Streamlit-based web interface:
  ```bash
   streamlit run app.py
   ```

---

## Example Data

The repository includes sample data for testing:

- `data/sample_doc.md`: A sample long document for question answering.
- `data/sample_table.csv`: Example tabular data for structured input.

You can replace these with your own documents or CSV files in the `data/` directory.

---

## Screenshots

Below is a screenshot of the Streamlit web interface:

![Streamlit UI](Screenshot%202025-06-04%20at%2011.11.05.png)

---

## Technologies Used

- **Sentence-BERT**: For generating semantic embeddings of text chunks.
- **FAISS**: For efficient vector similarity search.
- **HuggingFace Transformers (T5-small)**: For answer generation.
- **Streamlit**: For building the interactive web interface.
- **Python Libraries**: NumPy, Pandas, and others listed in `requirements.txt`.

---

## Project Structure

```
your-repo-name/
├── data/
│   ├── sample_doc.md        # Sample document for testing
│   ├── sample_table.csv     # Sample tabular data
├── Screenshot 2025-06-04 at 11.11.05.png  # UI screenshot
├── main.py                  # CLI script
├── app.py                   # Streamlit web app
├── requirements.txt         # Dependencies
└── README.md                # This file
```

---

## Usage

1. **Prepare Input**: Place your documents or CSV files in the `data/` directory.
2. **Run CLI or UI**:
   - Use `main.py` for terminal-based interaction.
   - Use `app.py` for the web interface.
3. **Ask Questions**: Input your questions via the CLI or Streamlit UI, and the system will retrieve relevant chunks and generate answers.

Example CLI usage:
```bash
python main.py --input data/sample_doc.md --question "What is the main topic?"
```

Example UI usage:
- Run `streamlit run app.py`.
- Upload a document or CSV via the web interface.
- Enter your question and view the generated answer.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows the project's style guidelines and includes tests where applicable.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or support, please open an issue on the [GitHub Issues page](https://github.com/your-username/your-repo-name/issues).
