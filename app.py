"User playing hangman in their browser"
"Relationship to routes_py => Sends HTTP requests to, HTTP/HTTPS"
"Relationship from routes_py - recieves feedback for the user and displays it"

from flask import Flask, redirect, url_for, request, render_template, session
from string import ascii_uppercase
import hangman_code.main
from  hangman_code.game import Game

app = Flask(__name__)
app.secret_key = "super-secret-key-change-this"

@app.route("/", methods=["GET"])
def index():
    game_data = session.get("game")
    
    if game_data is None:
        print ('No game yet')
        game_started = False
        word_template = ""
        score = None
        game_status = None
        game_name = None
        message = ""
        used_letters = []
        accepted_letters = []
    else:
        game = Game.from_dict(game_data)
        print ('in route/:', game.game_status.value,game.game_status.name)
        word_template = game.template
        score = game.score
        game_status = game.game_status.value
        message = game.message
        used_letters = game.used_letters or []
        accepted_letters = game.accepted_letters
        game_name = game.game_name
        game_started = True   # if we have a game, it’s started
        accepted_letters = game.accepted_letters

    return render_template(
        "index.html",
        message=message,
        template=word_template,
        accepted_letters=accepted_letters,
        used_letters=used_letters,
        lineLength=7,
        score=score,
        game_status=game_status,
        game_started=game_started,
        game_name=game_name,

    )

@app.route("/new_game", methods=["POST"])
def new_game():
    print('new game button pressed')
    new_game = Game()
    
    print(new_game.template)
    print(new_game.game_started)

    # ✅ keep key names consistent with index()
    session["game"] = new_game.to_dict()

    # ✅ reset everything for a fresh game
    #session["message"] = "hyjg"              # or "New game started!"
    #session["used_letters"] = []     # re-enable all buttons

    return redirect(url_for("index"))


@app.route("/name_game", methods=["POST"])
def name_game():
    # 1. Read the name from the form
    game_name = request.form.get("game_name", "").strip()
    print("Game name received:", game_name)

    # 2. Rebuild the current NEW_GAME object from session
    game_data = session.get("game")
    if not game_data:
        # No game started → redirect safely
        return redirect(url_for("index"))

    game = Game.from_dict(game_data)

    # 3. Update the game name and switch status to IN_PLAY
    game.game_name = game_name
    game.set_game_status(Game.Game_status.IN_PLAY)

    print (game.game_status)

    # 4. Store updated state back into session
    session["game"] = game.to_dict()
    print ('in name game:', game.game_status.value, game.game_status.name)

    # 5. Back to the main page
    return redirect(url_for("index"))



@app.route("/guess", methods=["POST"])
def guess():
    #from flask import request, session, redirect, url_for
    current_game = Game.from_dict(session["game"])
    # Get the letter from the form
    letter = request.form.get("letter")
    if not letter:
        print("⚠️ /guess called without 'letter'. FORM DATA:", request.form)
        return redirect(url_for("index"))

    # Normalize to uppercase (your letters list is A–Z)
    letter = letter.upper()
    print("Guessed:", letter)

    # Read current used letters from the session, add this one
    disabled = set(session.get("used_letters", []))
    disabled.add(letter)
    session["used_letters"] = list(disabled)

    # Your hangman logic
    template = hangman_code.main.guess(letter, "ABACUS")
    session["message"] = template

    # Debug: see what is now in the session
    print("Used letters now:", session["used_letters"])

    return redirect(url_for("index"))




@app.route("/show_line", methods=["POST"])
def show_line():
    print('Hello')
    return redirect(url_for("index"))




@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
"Relationship to main.py => Sends HTTP requests to, HTTP/HTTPS"
"Relationship from main.py - recieves feedback "
"for the user and displays it"



