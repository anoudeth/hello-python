import os
import google.genai as genai
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load variables from .env
load_dotenv()


def run_gemini_sample():
    # Now it pulls from the .env file
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY still not found. Check your .env file.")
        return

    # genai.configure(api_key=api_key)
    # model = genai.GenerativeModel('gemini-2.5-flash-lite')

    try:
        client = genai.Client(api_key=api_key)
        # response = model.generate_content("Explain RAG in one sentence.")
        response = client.models.generate_content(
            model='gemini-2.5-flash-lite',
            contents="Explain RAG in one sentence."
        )
        print(f"Response SDK: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_langchain():
    # Now it pulls from the .env file
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY still not found. Check your .env file.")
        return

    # genai.configure(api_key=api_key)
    # model = genai.GenerativeModel('gemini-2.5-flash-lite')

    try:
        # Configuration
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
        # Execution
        response = llm.invoke("Explain RAG in one sentence.")
        print(f"Response LangChain: {response.content}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_gemini_sample()
    run_langchain()