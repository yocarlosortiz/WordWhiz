WordWhiz
WordWhiz is a full-stack word-guessing game app where players crack the secret word, one letter at a time, using clever clues. The project features a Python FastAPI backend and a modern React + Tailwind CSS frontend.

Features
Fun word-guessing gameplay with clues and limited attempts
FastAPI backend for game logic and API endpoints
React frontend with a clean, responsive UI (Tailwind CSS)
CORS enabled for smooth local development
Easy local setup for both backend and frontend

Project Structure

Getting Started
1. Clone the Repository
WordWhiz
2. Backend Setup (FastAPI)
The backend API will be available at: http://localhost:8000
Interactive API docs: http://localhost:8000/docs
4. Frontend Setup (React)
The frontend will be available at: http://localhost:3000

How to Play
Click Start New Game.
Read the clue and guess letters one at a time.
You have 6 attempts to guess the word.
Win by revealing all letters before running out of attempts!

Tech Stack
Backend: Python, FastAPI, Uvicorn, Pydantic
Frontend: React, Tailwind CSS, JavaScript (ES6+)
Other: CORS, REST API

Development Notes
The backend uses in-memory storage for games (not persistent).
CORS is enabled for all origins for local development.
The frontend fetches from http://localhost:8000 by default.
