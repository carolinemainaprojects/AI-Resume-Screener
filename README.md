# 📄 AI Resume Screener

An AI-powered resume screening application that analyzes PDF resumes against job requirements and provides structured candidate insights.

## 🚀 Overview

The **AI Resume Screener** helps simplify the initial stage of candidate evaluation.

A user uploads a PDF resume and provides a job title and job description. The application extracts the resume text and uses **Google Gemini** to analyze the candidate's suitability for the role.

The system generates a structured evaluation including a resume score, job-match score, skills, strengths, weaknesses, and recommendations.

## 🔄 How It Works

```text
PDF Resume
    ↓
Upload Resume
    ↓
Extract Resume Text
    ↓
Google Gemini
    ↓
AI Evaluation
    ↓
┌─────────────────────────┐
│ Resume Score            │
│ Job Match Score         │
│ Skills                  │
│ Strengths               │
│ Weaknesses              │
│ Recommendations         │
└─────────────────────────┘
```

## ✨ Features

* 📄 PDF resume upload
* 🔍 Automatic resume text extraction
* 🤖 AI-powered candidate evaluation
* 📊 Resume scoring
* 🎯 Job-match assessment
* 🛠️ Skills identification
* 💪 Strengths analysis
* ⚠️ Weakness identification
* 💡 AI-generated recommendations
* 🌐 Streamlit web interface

## 🧪 Example Result

A resume evaluation can produce results such as:

```text
Resume Score: 92/100
Job Match: 95/100

Skills:
- Communication
- Research
- Project Management
- Data Analysis

Strengths:
- Strong alignment with the role
- Relevant professional experience
- Good technical and interpersonal skills

Areas for Improvement:
- Limited experience in some required technologies
```

The scores and recommendations are generated dynamically based on the uploaded resume and job description.

## 🛠️ Tech Stack

| Technology    | Purpose                    |
| ------------- | -------------------------- |
| Python        | Application logic          |
| Streamlit     | Web application interface  |
| Google Gemini | AI-powered resume analysis |
| PyPDF         | PDF text extraction        |
| python-dotenv | Environment configuration  |
| GitHub        | Version control            |

## 🔐 Security

API credentials are stored securely using environment variables or Streamlit secrets and are not included directly in the source code.

The `.gitignore` file helps prevent sensitive configuration files from being committed to the repository.

## 📁 Project Structure

```text
AI-Resume-Screener/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/carolinemainaprojects/AI-Resume-Screener.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your Gemini API key

Add your Gemini API key using the appropriate environment variable or Streamlit secrets configuration.

### 4. Run the application

```bash
streamlit run app.py
```

## 🎯 Business Value

Recruiters and hiring teams can receive a large number of applications for a single position.

This project demonstrates how Generative AI can assist with the initial screening process by quickly comparing candidate resumes with job requirements and highlighting relevant information.

The system is designed to **assist human decision-making rather than replace it**.

## 🔮 Future Improvements

* Multiple resume comparison
* Batch resume processing
* Candidate ranking
* CSV export
* Recruiter dashboard
* Database storage
* Automated email notifications
* ATS integration
* Candidate filtering by skills and experience

## 🌐 Live Demo

👉 **[AI Resume Screener — Live Demo](https://ai-resume-screener-dhhsbmjhkddjpz6tmjery3.streamlit.app/)**

## 👩🏽‍💻 Author

### Caroline Maina

**AI Automation & Generative AI**

**GitHub:** [@carolinemainaprojects](https://github.com/carolinemainaprojects)

**LinkedIn:** [Caroline Maina](https://www.linkedin.com/in/caroline-maina-480b74430/)

---

⭐ Explore my other AI automation projects on my GitHub profile.
