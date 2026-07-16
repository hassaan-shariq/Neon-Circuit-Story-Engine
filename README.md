# 🏎️ Neon Circuit Story Engine

> An AI-powered story generator set in the Neon Circuit universe — 
> a futuristic city where cars are alive and legends are born on the asphalt.

## 🔗 Live Demo
**[Open the Story Engine →](https://neon-circuit-story-engine-6zpjyefgkpkxbdkwn48s2d.streamlit.app/)**

---

## 📸 Preview

![Neon Circuit Story Engine](screenshot.png)

---

## ✨ What It Does

Enter a character name and car type to generate a cinematic, 
AI-powered story set in the Dravon universe's Neon Circuit — 
a futuristic racing world where every car has a personality, 
every district has a legend, and every race decides a fate.

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web interface |
| Groq API | AI story generation |
| LLaMA 3.1 | Language model |
| python-dotenv | Environment management |

---

## 🏗️ Architecture

The application separates UI from AI logic deliberately.
`app.py` handles all user interaction. `story_engine.py` 
handles all AI calls. Each layer can be upgraded independently.

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/hassaan-shariq/Neon-Circuit-Story-Engine.git
cd Neon-Circuit-Story-Engine
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**

Create a `.env` file:

Get a free key at [console.groq.com](https://console.groq.com)

**4. Run the app**
```bash
streamlit run app.py
```

---

## 🌆 The Neon Circuit Universe

The Neon Circuit is part of **Dravon** — a futuristic car-themed 
fictional universe where vehicles have personalities, districts 
pulse with neon light, and racing is the highest form of existence.

Districts include Nightshade, Voltspire, and Crimson Hollow.

---

## 👨‍💻 About The Developer

Built by **Hassaan Shariq** — a self-taught AI Engineer 
building real products and the Dravon universe from Karachi, Pakistan.

---
*Part of the Dravon Universe — Building the Neon Circuit, one story at a time.*
