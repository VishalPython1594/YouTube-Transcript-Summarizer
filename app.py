import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Getting the transcript data from You Tube videos

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split('=')[1]
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""  # Initialize an empty string for the final transcript
        for entry in transcript_data:
            transcript += " " + entry["text"]  # Correctly append each text entry
        
        return transcript.strip()  # Return the final transcript text
    
    except Exception as e:
        return f"Error: {e}"

prompt = '''You are a Youtube video summarizer. You will be taking the transcript text as input 
            and summarize the entire video capturing its essence and providing the key points that
            are highlighted in the video. You response should be point wise in 200-250 words.
            Please provide the summary of the transcript text appended here: '''

# Getting the summary based on prompt from Google Gemini Pro

def generate_gemini_content(transcript_text, prompt):

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt+transcript_text)
    return response.text

st.title('You Tube Transcript Summarizer from video URL')
youtube_link = st.text_input('Enter your YouTube Video link')

if youtube_link:
    video_id = youtube_link.split('=')[1]
    st.image(f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg', use_container_width = True)

if st.button('Get Summary Notes'):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown('## Summary')
        st.write(summary)