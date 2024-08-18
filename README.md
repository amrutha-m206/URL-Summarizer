
This end-to-end application provides concise summaries of YouTube videos or website content based on the links provided by the user. The app leverages the GROQ API for data retrieval and processing, and the Gemma Model for summarization.

## Features

- **YouTube Video Summarization:** Provide a YouTube video link to get a summary of the video content.
- **Website Content Summarization:** Provide a website URL to receive a summary of the text content.
- **Efficient Processing:** Uses the GROQ API for quick data retrieval and processing.
- **Accurate Summarization:** Powered by the Gemma Model for generating concise and accurate summaries.

## How It Works

1. **Input:** User provides a YouTube video link or a website URL.
2. **Data Retrieval:** The app uses the GROQ API to fetch the relevant content (e.g., video transcript or website text).
3. **Summarization:** The retrieved data is processed through the Gemma Model, which generates a summary.
4. **Output:** The user receives a brief and informative summary of the provided content.

## Technologies Used

- **GROQ API:** Utilized for retrieving and processing data from provided URLs.
- **Gemma Model:** The core model responsible for summarizing the retrieved content

## Libraries

The following libraries are required to run this application:

- `langchain`
- `langchain-community`
- `langchain-text-splitters`
- `validators==0.28.1`
- `youtube_transcript_api`
- `unstructured`
- `pytube`
- `nltk`
- `validators`
- `streamlit`
- `langchain_groq`

These dependencies are listed in the `requirements.txt` file.
