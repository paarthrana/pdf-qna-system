# 📄 PDF Q&A System

An AI-powered PDF Question & Answer System built using **Python**, **PyMuPDF**, and **Google Gemini API**.

This project allows users to ask questions about a PDF document and receive answers based only on the document's content. It also includes a PDF summarization feature.

---

## 🚀 Features

* 📖 Extract text from PDF documents
* ❓ Ask questions about the PDF
* 🤖 AI-generated answers using Gemini API
* 📝 Generate concise summaries of PDFs
* 🖥️ Interactive terminal-based interface
* 🔐 Secure API key management using `.env`

---

## 🛠️ Technologies Used

* Python
* Google Gemini API
* PyMuPDF (fitz)
* python-dotenv

---

## 📂 Project Structure

```
pdf-qna-system/
│
├── main.py
├── sample.pdf
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ How It Works

### Ask Questions

```
PDF
    ↓
Extract Text
    ↓
Gemini API
    ↓
Answer User Question
```

### Summarize PDF

```
PDF
    ↓
Extract Text
    ↓
Gemini API
    ↓
10-Point Summary
```

---

## ▶️ Running the Project

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies.

```
pip install -r requirements.txt
```

4. Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

5. Run the project.

```
python main.py
```

---

## 📌 Future Improvements

* Upload any PDF using user input
* Chat history
* PDF highlighting
* Chunking
* Embeddings
* Vector Database (FAISS / ChromaDB)
* Retrieval-Augmented Generation (RAG)
* Streamlit Web Interface

---

## 📚 Learning Outcomes

Through this project I learned:

* PDF processing using PyMuPDF
* Working with Document and Page objects
* Prompt Engineering
* Integrating Gemini API
* Building AI-powered document applications
* Writing modular and reusable Python code

---

## 👨‍💻 Author

**Paarth Rana**

B.Tech CSE (AI & ML)

