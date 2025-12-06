# Pythonman - AI Python Beginner Tutor

A basic AI tutor capable of teaching Python basics made for my AI class  
It uses GPT-4o to explain concepts, debug code, generate exercises, and give feedback.

## Features
- Concept explanations (variables, loops, functions, etc.)
- Code example generation
- Debugging assistance
- Practice exercise generation
- Adaptive feedback based on user input
- Intent detection through simple rule-based system

## Files
- `main.py` — Main application loop and GPT-4o interaction.
- `thinking.py` — Simple intent detection module.

## Requirements
- Python 3.10+
- openai library (`pip install openai`)
- Valid OpenAI API key (set as environment variable: `OPENAI_API_KEY`)

## Setting Your OpenAI API Key

This project uses the OpenAI API.  
Before running the tutor, set your API key as an environment variable.

### Windows PowerShell
```bash
$env:OPENAI_API_KEY="your_api_key_here"
```

### Mac / Linux
```bash
export OPENAI_API_KEY="your_api_key_here"
```

The program will automatically read the key using:
client = OpenAI()

## Run the tutor
```bash
$env:OPENAI_API_KEY="your_key_here"
python main.py
```
