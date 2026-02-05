import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


def run_gemini_sample():
    # Now it pulls from the .env file
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY still not found. Check your .env file.")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash-lite')

    try:
        response = model.generate_content("convert this Lao name 'ບ້ານສະຫວ່າງ' to Karaoke")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_gemini_sample()