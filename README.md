# 🎥 YouTube Transcript Summarizer - AI-Powered Video Insights  

## 📌 Project Overview  
This project is an **AI-powered YouTube transcript summarizer** that extracts **video transcripts** and generates concise **key-point summaries** using **Google Gemini AI**. It helps users **quickly understand** long YouTube videos without watching them entirely.

✅ **Enter a YouTube video link, and the AI generates:**  
- 📜 **Transcript extraction from YouTube videos**  
- 📝 **Concise AI-powered summary (200-250 words)**  
- 🔹 **Key takeaways formatted in bullet points**  

This tool is ideal for **students, professionals, and content creators** who need **quick insights from long videos.**  

---

## 📊 Technologies Used  
- **Python** (Backend)  
- **Streamlit** (Web App Interface)  
- **Google Gemini Pro API** (LLM-based summarization)  
- **YouTube Transcript API** (Extracts video transcripts)  
- **Hugging Face Cloud** (Deployment platform)  
- **Dotenv** (Environment variable management)  

---

## ⚙️ Installation & Setup  

### **1️⃣ Clone the repository**  
```bash
git clone https://github.com/VishalPython1594/YouTube-Transcript-Summarizer.git
cd YouTube-Transcript-Summarizer
```

### **2️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set up API Keys**
* Obtain a Google Gemini API Key from Google AI Studio
* Add the API key to a .env file in the project directory:
```bash
GOOGLE_API_KEY=your_google_api_key
```

### **4️⃣ Run the Streamlit app**
```bash
streamlit run app.py
```

## **🏗️ Project Workflow**:
1️⃣ User enters a YouTube video URL.
2️⃣ The YouTube Transcript API extracts the video's transcript.
3️⃣ Gemini AI processes the transcript & generates a concise summary.
4️⃣ The summary is displayed in bullet points.

## **🖥️ Usage**:
1. Run the app:
```bash
streamlit run app.py
```

2. Enter a YouTube video link.
3. Click "Get Summary Notes" to extract & summarize.
4. View the AI-generated summary with key points.

## **📊 Sample Output**:
![yt_1](https://github.com/user-attachments/assets/e932fcfd-779f-4de9-8424-d37e40ca2199)
![yt_2](https://github.com/user-attachments/assets/d5bdaf32-b0c7-41af-804a-2100c834ebc3)
![yt_3](https://github.com/user-attachments/assets/379dccf1-3044-4770-a7f4-4050a6dbbf22)
