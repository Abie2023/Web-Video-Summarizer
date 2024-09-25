import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google Gemini
def configure_genai(api_key):
    genai.configure(api_key=api_key)

# Extract text from website
def extract_website_text(website_url):
    try:
        response = requests.get(website_url)
        response.raise_for_status()  # Ensure we handle HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        website_text = " ".join([para.get_text() for para in paragraphs])
        return website_text
    except requests.RequestException as req_error:
        print(f"Request error: {req_error}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Generate summary using Google Gemini
def generate_gemini_summary(website_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + website_text)
    return response.text

# Summarize website content
def summarize_website_content(website_url, prompt):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set GOOGLE_API_KEY in your .env file.")
    
    configure_genai(api_key)
    website_text = extract_website_text(website_url)
    summary = generate_gemini_summary(website_text, prompt)
    return summary
