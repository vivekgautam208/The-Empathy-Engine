# Empathy Engine – Giving AI a Human Voice

## Project Overview

**Empathy Engine** is an AI-powered application that converts text into speech while adapting the voice characteristics based on the emotional tone of the input text. Traditional Text-to-Speech (TTS) systems often sound robotic and lack emotional variation. This project improves user interaction by detecting emotions from text and adjusting the generated voice accordingly.

The system analyzes the sentiment of the text and classifies it into three categories: **Positive, Negative, or Neutral**. Based on the detected emotion, the application modifies the speech characteristics (such as speed) before generating the final audio output.

This project demonstrates how AI can make voice interactions more natural and expressive.

Project Screenshots

Below are some screenshots demonstrating the working of the Empathy Engine web interface.

1. Application Interface




2. Text Input and Emotion Detection




3. Generated Voice Output

---

# Technologies Used

### Programming Language

* **Python**

### Web Framework

* **Flask** – Used to create a web interface where users can enter text and listen to generated speech.

### Sentiment Analysis

* **VADER Sentiment Analyzer** (from the `vaderSentiment` library)
  Used to detect the emotional tone of the input text.

### Text-to-Speech Engine

* **gTTS (Google Text-to-Speech)**
  Used to convert the text into an audio file.

### Frontend

* **HTML**
* **CSS**
* **Jinja2 Template Engine** (used with Flask)

### Additional Tools

* **UUID** – Used to generate unique filenames for audio files to avoid caching issues.
* **Flask Static Folder** – Used to store generated audio files.

---

# How the System Works

The Empathy Engine follows these steps:

### 1. Text Input

The user enters a sentence or paragraph in the web interface.

### 2. Emotion Detection

The system analyzes the text using the **VADER Sentiment Analyzer** and calculates a sentiment score.

### 3. Emotion Classification

The sentiment score is classified into three categories:

* **Positive**
* **Negative**
* **Neutral**

### 4. Voice Parameter Mapping

Based on the detected emotion, the system modifies the speech parameters:

| Emotion  | Speech Speed |
| -------- | ------------ |
| Positive | Faster voice |
| Negative | Slower voice |
| Neutral  | Normal speed |

### 5. Speech Generation

The system uses **Google Text-to-Speech (gTTS)** to generate an audio file.

### 6. Audio Playback

The generated audio file is displayed in the web interface using an **HTML audio player**, allowing the user to listen to the voice output.

---

# Project Folder Structure

```
empathy-engine/
│
├── app.py
│
├── static
│   └── audio
│
└── templates
    └── index.html
```

---

# Installation and Setup

### Step 1 – Clone the Repository

```
git clone https://github.com/your-username/empathy-engine.git
cd empathy-engine
```

---

### Step 2 – Install Required Libraries

Install the required Python libraries using pip:

```
pip install flask gTTS vaderSentiment
```

---

### Step 3 – Run the Application

Start the Flask server:

```
python app.py
```

---

### Step 4 – Open the Web Interface

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

# Example Usage

Example input:

```
I am very happy to help you today!
```

Output:

```
Detected Emotion: Positive
```

The system then generates an audio file and plays it using the web audio player.

---

# Design Choices

### Emotion Detection

VADER was selected because it is lightweight and works well for short text inputs.

### Text-to-Speech Engine

gTTS was chosen because it produces natural speech and is easy to integrate with Python.

### Unique Audio File Generation

Unique file names are generated using UUID to prevent browser caching issues and ensure that new audio is played for each request.

### Web Interface

Flask was used to build a simple and interactive interface that allows users to easily test the system.

---

# Future Improvements

Possible improvements include:

* Detecting **more granular emotions** (happy, sad, angry, surprised).
* Adding **pitch and volume control** for better emotional expression.
* Integrating **advanced neural voice models** such as ElevenLabs.
* Adding **real-time voice waveform visualization**.
* Supporting **multiple languages and voice styles**.

---

# Author

**Vivek Gautam**

Empathy Engine – AI Emotion-Based Voice Generation Project
