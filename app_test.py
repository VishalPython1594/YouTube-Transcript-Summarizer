import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

# Configure Google API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract transcript from a YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split('=')[1]

        # Check if transcripts are available
        available_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Fetch transcript (auto-generated or manually provided)
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = " ".join([entry["text"] for entry in transcript_data])  # Efficient joining
        return transcript.strip()
    
    except TranscriptsDisabled:
        st.error("Transcripts are disabled for this video. Try another video.")
        return None
    except NoTranscriptFound:
        st.error("No transcript found for this video. Try another video.")
        return None
    except Exception as e:
        st.error(f"Error extracting transcript: {e}")
        return None

# Prompt for Gemini
prompt = '''You are a YouTube video summarizer. You will be taking the transcript text as input 
            and summarize the entire video capturing its essence and providing the key points that
            are highlighted in the video. Your response should be point-wise in 200-250 words.
            Please provide the summary of the transcript text appended here: '''

# Function to generate summary using Google Gemini API
def generate_gemini_content(transcript_text, prompt):
    try:
        if not transcript_text.strip():
            return "Error: No transcript text available for summarization."

        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt + transcript_text)
        return response.text if response else "Error: No response from the model."
    
    except Exception as e:
        return f"Error generating summary: {e}"

# Streamlit App UI
st.title('YouTube Transcript Summarizer')
youtube_link = st.text_input('Enter your YouTube Video link')

if youtube_link:
    video_id = youtube_link.split('=')[1]
    st.image(f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg', use_container_width=True)

if st.button('Get Summary Notes'):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        st.write("✅ Transcript extracted successfully!")  # Debugging log
        st.text_area("Extracted Transcript", transcript_text[:1000] + "...", height=150)  # Show first 1000 chars
        
        summary = generate_gemini_content(transcript_text, prompt)
        
        if "Error" in summary:
            st.error(summary)
        else:
            st.markdown('## Summary')
            st.write(summary)
    else:
        st.error("⚠️ Failed to extract transcript. Please check if captions are available for this video.")
