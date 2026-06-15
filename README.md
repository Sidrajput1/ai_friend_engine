# My AI Friend 🤖❤️

An AI-powered virtual friend built with FastAPI, Next.js, Gemini, Ollama, and Retrieval-Augmented Generation (RAG).

Rahul is designed to behave like a supportive friend who remembers important information, maintains conversational context, and responds naturally in Hinglish.

---

## Features

### AI Friend Persona

* Custom personality system
* Hinglish conversation style
* Short, friendly responses
* Context-aware interactions

### Long-Term Memory

* Memory extraction from conversations
* Semantic memory retrieval
* Vector search using ChromaDB
* User preference and goal tracking

### Short-Term Memory

* Conversation history tracking
* Context preservation
* Session-based chat memory

### RAG Pipeline

* Memory retrieval before response generation
* Context injection into prompts
* Personalized responses

### Multi-LLM Support

* Gemini API support
* Ollama local models support
* Easy provider switching

### Workflow Routing

The system automatically routes user questions to:

* General Chat Workflow
* Memory Workflow
* History Workflow

### Frontend

* Next.js App Router
* ChatGPT-style interface
* Auto-scroll messages
* Loading states
* Session persistence
* Responsive design

---

## Tech Stack

### Frontend

* Next.js
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python

### AI

* Gemini API
* Ollama
* Prompt Engineering
* Persona Engineering

### Memory & Retrieval

* ChromaDB
* Embeddings
* RAG

---

## Project Architecture

User
↓
Next.js Frontend
↓
FastAPI Backend
↓
Workflow Router
↓
Memory Retrieval (ChromaDB)
↓
Prompt Builder
↓
Gemini / Ollama
↓
Response

---

## Example Conversation

User:

> I failed my interview.

Rahul:

> Arre bhai 😔
> Tension mat le.
> Next baar phod denge 💪

User:

> What is my goal?

Rahul:

> Bhai tera goal full-stack developer banna hai 🚀

---

## Local Setup

### Clone Repository

```bash
git clone <your-repository-url>
cd rahul-ai-friend
```

### Backend Setup

```bash
python -m venv .venv
```

Activate environment:

```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
GEMINI_API_KEY=your_api_key
USE_OLLAMA=false
```

Run FastAPI:

```bash
uvicorn api.main:app --reload
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Future Improvements

* LangGraph Integration
* Tool Calling
* Streaming Responses
* MongoDB Chat Persistence
* Authentication
* Multi-Persona Support
* Voice Conversations

---

## What I Learned

This project helped me learn:

* FastAPI
* Next.js
* Prompt Engineering
* Persona Engineering
* RAG Architecture
* Vector Databases
* ChromaDB
* Memory Systems
* Gemini API Integration
* Ollama Integration
* Workflow-based AI Design

---

## Author

Sidharth Shekhar

Full Stack Developer (MERN) exploring AI Engineering, RAG, and Agentic AI systems.
