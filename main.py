from google import genai
from dotenv import load_dotenv
import os
import fitz # type: ignore

def load_api():
    load_dotenv()
    api_key =os.getenv("GEMINI_API_KEY")
    client=genai.Client(api_key=api_key)
    return client

def extract_text(pdf_path):
    pdf=fitz.open(pdf_path)
    pdf_text=""
    for page in pdf:
        page_text=page.get_text()
        pdf_text+=page_text
    pdf.close()
    return pdf_text

def summarise_text(client,pdf_text):
    prompt = f"""
    You are a helpful study assistant.

    Summarize the following document in 10 concise bullet points
    for a first-year engineering student.

    Document:
        {pdf_text}
    """
    summary=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return summary.text

def ask_question(client,pdf_text,question):
    prompt=f""" you are answering a question from the document.
    answer ONLY with information provided in document,if answer is not found in it
    just reply: "Answer not found in the document"
    document:{pdf_text}
    question:{question}
"""
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def main():
    client=load_api()
    pdf_path="prompts.pdf"
    pdf_text=extract_text(pdf_path)
    while True:
        print("======================PDF-QNA-SYSTEM============================")
        print("type exit to quit ")
        question=input("Ask anything from the pdf: ")
        if question.lower()=="exit":
            break
        answer=ask_question(client,pdf_text,question)
        print(answer)


if __name__=="__main__":
    main()
