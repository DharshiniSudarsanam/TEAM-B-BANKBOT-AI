BankBot – Banking FAQ Chatbot

BankBot is a **secure, domain-restricted banking FAQ chatbot** built using **Streamlit**, **Ollama**, and **Python**.
It answers **only banking-related questions** and blocks all unrelated queries.

 Features

* Banking-only FAQ responses
* Non-banking query restriction
* Local LLM using Ollama
* Simple Streamlit UI

 Tech Stack

* Streamlit
* Python
* Ollama (LLM)
* Custom filtering logic

 Working

User Query → Banking Filter → Ollama → Safe Response

 Run

ollama run llama3
streamlit run app.py

 Note

Prototype for secure banking assistance; no real bank integration.

