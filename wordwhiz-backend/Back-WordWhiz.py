# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GuessRequest(BaseModel):
    game_id: str
    letter: str

WORDS = [
    {"word": "python", "clue": "A popular programming language."},
    {"word": "giraffe", "clue": "Tallest land animal."},
    {"word": "eclipse", "clue": "When the moon blocks the sun."},
]

games = {}

def mask_word(word, guesses):
    return " ".join([c if c in guesses else "_" for c in word])

@app.post("/start")
def start_game():
    entry = random.choice(WORDS)
    game_id = str(random.randint(1000, 9999))
    games[game_id] = {
        "word": entry["word"],
        "clue": entry["clue"],
        "guesses": set(entry["word"][0]),
        "attempts_left": 6,
        "status": "playing"
    }
    return {
        "game_id": game_id,
        "clue": entry["clue"],
        "first_letter": entry["word"][0],
        "word_mask": mask_word(entry["word"], games[game_id]["guesses"]),
        "attempts_left": 6
    }

@app.post("/guess")
def guess(req: GuessRequest):
    game = games.get(req.game_id)
    if not game or game["status"] != "playing":
        raise HTTPException(status_code=404, detail="Game not found or finished")

    letter = req.letter.lower()
    if letter in game["guesses"]:
        return {
            "word_mask": mask_word(game["word"], game["guesses"]),
            "attempts_left": game["attempts_left"],
            "status": game["status"],
            "message": "Letter already guessed."
        }

    if letter in game["word"]:
        game["guesses"].add(letter)
    else:
        game["attempts_left"] -= 1

    word_mask = mask_word(game["word"], game["guesses"])
    if "_" not in word_mask.replace(" ", ""):
        game["status"] = "won"
    elif game["attempts_left"] <= 0:
        game["status"] = "lost"

    return {
        "word_mask": word_mask,
        "attempts_left": game["attempts_left"],
        "status": game["status"],
        "message": "Correct!" if letter in game["word"] else "Incorrect!"
    }
