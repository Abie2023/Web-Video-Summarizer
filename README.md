# NotaViva
NotaViva is a YouTube Transcript to Detailed Notes Converter. This application uses Google Gemma2 Transformer to summarize YouTube video transcripts and provides the summary in PDF format. Currently, it supports only English videos.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/notaviva.git
    ```
    ```
    cd notaviva
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```
    ```
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Google API key:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
