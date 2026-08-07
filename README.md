# 🛡️ ScamShield AI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Caspian SDK](https://img.shields.io/badge/Caspian-SDK-green)
![License](https://img.shields.io/badge/License-MIT-blue)

> **An AI-powered phishing and scam detection assistant built with Flask, Google Gemini, and the Caspian SDK.**

ScamShield AI helps users identify phishing messages, scam emails, fake job offers, malicious URLs, and other online fraud attempts using AI-powered analysis. It provides a structured risk assessment, explains suspicious indicators, offers safety recommendations, and generates downloadable PDF reports.

The project demonstrates how AI agents can leverage the **Caspian SDK** as a communication layer while integrating modern LLM capabilities through **Google Gemini**.

---

# 📌 Problem Statement

Millions of users receive fraudulent messages every day through emails, SMS, messaging platforms, and websites. Most users cannot easily determine whether a message is genuine or malicious.

ScamShield AI aims to provide an intelligent assistant that quickly analyzes suspicious content and helps users make safer decisions before interacting with potential scams.

> **This project was developed as a Minimum Viable Product (MVP) for the Caspian AI Internship Challenge.**

---

# ✨ Key Features

* 🤖 AI-powered scam message classification
* 🔗 Suspicious URL detection
* 📊 Risk score with confidence estimation
* 🚩 Scam keyword identification
* 💡 Personalized cybersecurity recommendations
* 📄 Downloadable PDF investigation report
* 📧 Caspian SDK Email integration
* 🎨 Responsive Flask web interface

---

# 🏗️ Architecture

```text
                 User
                   │
                   ▼
          Flask Web Application
                   │
     ┌─────────────┼──────────────┐
     │             │              │
     ▼             ▼              ▼
 Message      URL Analyzer    PDF Generator
 Analysis
     │
     ▼
 Google Gemini AI
     │
     ▼
 Caspian SDK
     │
     ▼
 Email Channel
```

---

# ⚙️ Technology Stack

## Backend

* Python
* Flask

## Artificial Intelligence

* Google Gemini API

## Communication Layer

* Caspian SDK

## Report Generation

* ReportLab

## Frontend

* HTML
* CSS
* JavaScript

---

# 📸 Application Preview

## 🏠 Home Page

![Home](assets/home.png)

---

## 🤖 Workflow

![Workflow](assets/workflow.png)

---

## 🔗  Analysis

![Analyze](assets/analyze.png)

---

# 🎥 Demo

ScamShield AI can analyze:

* Scam Messages
* Phishing Emails
* Suspicious URLs

and generate an AI-powered PDF report containing risk assessment, explanations, and safety recommendations.

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/student-mitali/ScamShield-AI.git

cd ScamShield-AI
```

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

CASPIAN_API_KEY=YOUR_CASPIAN_API_KEY

CASPIAN_BASE_URL=YOUR_CASPIAN_BASE_URL
```

---

# ▶️ Running the Application

```bash
python app.py
```

Visit:

```text
http://127.0.0.1:5000
```

---

# 📧 Caspian SDK Integration

ScamShield AI integrates the **Caspian SDK** as its communication layer.

Current MVP supports:

* ✅ Email communication via Caspian SDK

The architecture is modular and can be extended to additional Caspian-supported communication channels such as Telegram, Discord, Slack, and SMS.

---

# 🌐 Why Caspian?

ScamShield AI uses the Caspian SDK as its communication layer, allowing AI-powered scam detection to integrate seamlessly with messaging workflows.

Rather than implementing platform-specific communication logic, Caspian provides a unified interface for handling communications, making the scam detection engine reusable and extensible across multiple channels.

---

# 📄 PDF Report

Each analysis can be exported as a PDF containing:

* Risk Level
* Scam Category
* AI Explanation
* Suspicious Indicators
* Safety Recommendations

---

# 📂 Project Structure

```text
ScamShield-AI
│
├── app.py
├── analyzer.py
├── handler.py
├── pdf_generator.py
├── config.py
├── prompts.py
│
├── channels/
│   └── caspian_email.py
│
├── services/
│   └── url_analyzer.py
│
├── templates/
├── static/
├── assets/
├── utils/
│
├── requirements.txt
└── README.md
```

---

# 🏆 Accomplishments

* Built an end-to-end AI-powered scam detection platform.
* Integrated Google Gemini for intelligent scam analysis.
* Implemented suspicious URL analysis.
* Added downloadable PDF investigation reports.
* Integrated the Caspian SDK as the communication layer.
* Delivered a functional MVP focused on solving a real-world cybersecurity problem.

---

# 📚 Challenges

* Designing a modular architecture for future multi-channel communication.
* Integrating AI analysis into a lightweight Flask application.
* Managing external APIs and environment configuration.
* Delivering a functional MVP within a limited development timeline.

---

# 📖 What We Learned

Through this project we gained hands-on experience with:

* AI application development using Google Gemini
* Flask backend architecture
* Prompt engineering
* REST API integration
* Environment management
* Communication-layer design using the Caspian SDK
* Building production-oriented MVPs under tight deadlines

---

# 🔮 Future Improvements

* Multi-channel Caspian integration (Telegram, Discord, Slack, SMS)
* OCR support for scam screenshots
* Browser extension
* Real-time phishing detection
* User authentication
* Scam history dashboard
* Community-powered scam reporting

---

# 👩‍💻 Author

**Mitali Devda**

GitHub: https://github.com/student-mitali

---

# 📜 License

This project was developed for educational, open-source, and hackathon purposes.
