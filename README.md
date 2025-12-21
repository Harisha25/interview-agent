
# Interview Practice Partner – AI Conversational Agent (Groq)

This project is an AI-powered Interview Practice Agent that helps users prepare for job interviews through natural, interactive conversations. The agent simulates a realistic interviewer, asks follow-up questions, evaluates answers, and provides feedback. It uses GroqCloud’s Llama 3.1 models for fast and free inference.

## Features

✔ Mock interview simulator
✔ Role-specific questions
✔ Follow-up questions like real interviews
✔ Feedback on user responses
✔ Handles multiple personas (confused, efficient, chatty, edge-case)
✔ Continuous conversation until user types “exit”

## Architecture Overview

User Input → Groq Llama 3.1 Model → main.py → Agent Response

Components:

* main.py
* Groq SDK
* requirements.txt
* README.md

##  How it Works

1. User chooses interview role
2. Agent asks intro and technical questions
3. Agent asks follow-up questions
4. User can request feedback anytime
5. Agent continues until user types "exit"

##  Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/Harisha25/interview-agent.git
cd interview-agent/interview_agent
```

### 2. Create Virtual Environment

```
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
pip install groq
```

### 4. Set Groq API Key

Get your key from: [https://console.groq.com/keys](https://console.groq.com/keys)

CMD:

```
set GROQ_API_KEY=your_key_here
```

PowerShell:

```
$env:GROQ_API_KEY="your_key_here"
```

##  Run the Agent

```
python main.py
```

Example:

```
Interview Practice Agent Started. Type 'exit' to quit.
You:
```

##  Sample Commands

Start interview:

```
I want to practice for a backend developer role.
```

Confused user:

```
I don't understand this question.
```

Chatty user:

```
Tell me a joke before we continue.
```

Efficient user:

```
Give me short questions only.
```

Feedback:

```
Give feedback on my answers.
```

Stop interview:

```
exit
```


##  Design Decisions

* Groq used instead of OpenAI for free & fast inference
* Llama-3.1-8b-instant model chosen for speed
* Loop-based architecture for simplicity
* Supports multi-role interview types
* Designed to meet all assignment requirements

##  File Structure

```
interview_agent/
main.py
requirements.txt
README.md
.gitignore
env/ (ignored)
```

##  Made by

**G. Harisha (Jain University)**
Interview Practice Partner – Eightfold AI Agent Assignment



