Full-stack word-guessing game app where players crack the secret word, one letter at a time, using clever clues. The project features a Python FastAPI backend and a modern React + Tailwind CSS frontend.

Features
- Fun word-guessing gameplay with clues and limited attempt
- FastAPI backend for game logic and API endpoints
- React frontend with a clean, responsive UI (Tailwind CSS)
- CORS enabled for smooth local development
- Easy local setup for both backend and frontend

How to Play
1. Click Start New Game.
2. Read the clue and guess letters one at a time.
3. You have 6 attempts to guess the word.
4. Win by revealing all letters before running out of attempts!

Tech Stack
- Backend: Python, FastAPI, Uvicorn, Pydantic
- Frontend: React, Tailwind CSS, JavaScript (ES6+)
- Other: CORS, REST API

Development Notes: 
1. The backend uses in-memory storage for games (not persistent).
2. CORS is enabled for all origins for local development.
3. The frontend fetches from http://localhost:8000 by default.
4. Clone the Repository "WordWhiz
5. The backend API (FASTAPI) will be available at: http://localhost:8000
6. Interactive API docs: http://localhost:8000/docs
7. The frontend(React) will be available at: http://localhost:3000
