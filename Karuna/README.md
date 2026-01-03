BankBot AI – System Architecture
1. Overview

BankBot AI is an intelligent banking chatbot built using Python and Ollama.
It provides banking-related assistance through local AI inference, ensuring privacy and offline capability.

2. Key Components

User Interface
Accepts user queries and displays chatbot responses.

Application Controller (app.py)
Manages user input, intent handling, AI interaction, and output display.

AI Engine (Ollama)
Runs a local language model to generate natural language responses.

Intent Detection Module
Identifies the type of banking query and routes it accordingly.

Banking Logic Module
Handles banking-related responses and formats outputs.

Data Storage
Stores chat history locally using JSON or SQLite.

Input Validation
Ensures safe and valid user input.

3. Working Flow

User enters a query

Input is validated

Intent is detected

Query is sent to Ollama

AI response is generated

Response is displayed and saved

4. Technology Stack

Language: Python

AI Engine: Ollama

Storage: JSON / SQLite

Libraries: requests, logging, re