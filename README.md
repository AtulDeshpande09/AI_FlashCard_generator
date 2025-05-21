# 🧠 AI-Powered Flashcard & Quiz Generator

Turn any block of text into intelligent, cloze-style flashcards using natural language processing (NLP). Perfect for students, educators, and self-learners. Built with `Flask`, powered by `nltk`, and exports directly to `Anki` decks.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Flask](https://img.shields.io/badge/Flask-Web%20App-ff69b4)

---

## ✨ Features

- **Named Entity Recognition (NER)** to generate meaningful question-answer pairs
- **Cloze deletion (fill-in-the-blank)** format for deeper learning
- **One-click Anki deck export** (`.apkg`) for long-term retention
- Minimalist and responsive **web interface**
- 100% offline and open-source

---

## 🖼️ Demo

> Paste in any paragraph.  
> Instantly generate intelligent flashcards.  
> Export to Anki. Done.

![demo](https://user-images.githubusercontent.com/demo-gif-placeholder.gif)  
*(Coming soon: Live demo & screenshots)*

---

## ⚙️ How It Works

1. Input any text (article, notes, etc.).
2. The app uses **nltk's NER** to identify important concepts.
3. Flashcards are created by **blanking out** named entities.
4. You can view them in-browser or **export to Anki**.

---

## 🚀 Getting Started

### 1. Clone & Install

```bash
git clone https://github.com/yourusername/flashcard-generator.git
cd flashcard-generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📦 Export to Anki

You can download the generated flashcards as a .apkg file that works directly with Anki, the most popular spaced repetition software.


---

## 🧠 Example

Input:

> Albert Einstein was born in Ulm, Germany in 1879.



Output:

> Q: _____ was born in Ulm, Germany in 1879.
A: Albert Einstein




---

## 📁 Project Structure

flashcard-generator/
├── app.py
├── templates/
│   ├── index.html
│   └── flashcard.html
├── static/               # (optional assets)
├── requirements.txt
└── flashcards.apkg       # generated output


---

## ✅ To-Do

[ ] Flashcard editing before download

[ ] Language detection & multilingual support

[ ] UI enhancements

[ ] Support for PDFs or copied lecture notes



---

## ⚖️ License

This project is licensed under the MIT License.
Feel free to use, modify, and share!


---
