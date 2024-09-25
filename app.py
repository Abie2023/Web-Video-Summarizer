import streamlit as st
from dotenv import load_dotenv
import os
from youtube_summarizer import configure_genai, extract_transcript_details, generate_gemini_content
from website_summarizer import summarize_website_content
from fpdf import FPDF

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
configure_genai(GOOGLE_API_KEY)

# Prompt templates for summarization
youtube_prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
in 250 words. Please provide the summary of the text given here:  """

website_prompt = "Summarize the main points of this website in short : "

# Function to create a PDF
def create_pdf(summary, file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("helvetica", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf.output(file_path)

# Streamlit App
st.title("🗲 Save Time With: NotaViva 🤌")
st.markdown("**Currently available for English videos only**")

# Sidebar for selection
option = st.sidebar.radio(
    "Choose an option:",
    ["YouTube Video Summarizer", "Website Content Summarizer"]
)

if option == "YouTube Video Summarizer":
    st.subheader("YouTube Video Summarizer")
    youtube_link = st.text_input("Enter YouTube Video Link:")
    
    if youtube_link:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("Get Detailed Notes"):
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            summary = generate_gemini_content(transcript_text, youtube_prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)

            pdf_file_path = "detailed_notes.pdf"
            create_pdf(summary, pdf_file_path)
            with open(pdf_file_path, "rb") as pdf_file:
                st.download_button(label="Download PDF", data=pdf_file, file_name=pdf_file_path, mime="application/pdf")

elif option == "Website Content Summarizer":
    st.subheader("Website Content Summarizer")
    website_url = st.text_input("Enter Website URL:")
    
    if website_url:
        website_summary = summarize_website_content(website_url, website_prompt)
        st.markdown("## Website Content Summary:")
        st.write(website_summary)
