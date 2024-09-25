# NotaViva
NotaViva is a YouTube Transcript and Website content to Detailed Notes Converter. This application uses Google Gemini-1.5pro/flash Transformer to summarize YouTube video transcripts and provides the summary in PDF format.

## Installation

1. Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/notaviva.git](https://github.com/Abie2023/Web-Video-Summarizer.git)
    ```
    ```
    cd Web-Video-Summarizer
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```
    ```
    source venv/bin/activate   #unix systems
    ```
    ```
   venv\Scripts\activate  # On Windows use
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Google API key:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ```

5. Start the app
   ```
   streamlit run app.py
   ```
