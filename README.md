# 🧠 Crew_AI_Agent – Article Summarizer

**Crew_AI_Agent** is a minimal AI agent built with **CrewAI** to summarize online articles in **≤ 100 words**.
It takes a URL as input, searches the article content, and generates a concise summary using **GPT-4o-mini**.

🎥 **Demo**: [https://youtu.be/Tyx_s82tG5M](https://youtu.be/Tyx_s82tG5M)

---

## ✨ What It Does

* Accepts an article URL
* Searches and extracts relevant content
* Generates a short, clear summary (≤ 100 words)
* Runs from the command line

---

## 🧠 Why CrewAI?

CrewAI was used to **model the task as an AI agent**, not just a prompt:

* Clear **agent role** (Article Summarizer)
* Explicit **goal** and **task definition**
* Built-in **tool usage** (website search)
* Easy to extend into **multi-agent workflows** later (e.g., extract → summarize → validate)

This makes the system more **modular, explainable, and production-ready** than a single LLM call.

---

## 📊 Why CrewAI Observability?

CrewAI’s observability (`tracing=True`) was enabled to:

* Track how the agent reasons about the task
* Inspect tool usage and execution flow
* Debug agent behavior
* Support future optimization and scaling

This is especially useful when building **real-world AI agents**, not just demos.

---

## 🧱 Tech Stack

* Python
* CrewAI
* GPT-4o-mini
* crewai-tools
* python-dotenv

---

## ▶️ How to Run

```bash
pip install crewai crewai-tools python-dotenv
python main.py
```

Add your OpenAI key to `.env`:

```env
OPENAI_API_KEY=your_key_here
```

---

## 🎯 Use Cases

* News & blog summarization
* Research reading assistance
* Preprocessing for RAG pipelines
* Agent-based AI experiments
 
