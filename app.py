"User playing hangman in their browser"
"Relationship to routes_py => Sends HTTP requests to, HTTP/HTTPS"
"Relationship from routes_py - recieves feedback for the user and displays it"

from flask import Flask, redirect, url_for, request, render_template, session
from string import ascii_uppercase
import hangman_code.main
from  hangman_code.game import Game

app = Flask(__name__)
app.secret_key = "super-secret-key-change-this"


## This runs every time one of the other routes is called 
@app.route("/", methods=["GET"])
def index():
    game_data = session.get("game")

    if game_data is None:
        print ('No game yet')
        game_started = False
        template = None
        score = None
        game_status = None
        game_name = None
        message = ""
        used_letters = []
        accepted_letters = []
    else:
        game = Game.from_dict(game_data)
        print ('in route/:', game.game_status.value,game.game_status.name)
        template = game.template
        score = game.score
        game_status = game.game_status.value
        message = game.message
        used_letters = game.used_letters or []
        accepted_letters = game.accepted_letters
        game_name = game.get_game_name()
        game_started = True   # if we have a game, it’s started
        accepted_letters = game.accepted_letters

    return render_template(
        "index.html",
        message=message,
        template=template,
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

    new_game = Game()
    session["game"] = new_game.to_dict()
    return redirect(url_for("index"))


@app.route("/name_game", methods=["POST"])
def name_game():
    # 1. Read the name from the form
    game_name = request.form.get("game_name", "").strip()

    # 2. Rebuild the current NEW_GAME object from session
    current_game = session.get("game")
    if not current_game:
        # No game started → redirect safely
        return redirect(url_for("index"))

    game = Game.from_dict(current_game)

    # 3. Update the game name and switch status to IN_PLAY
    game.set_game_name (game_name)
    game.set_game_status(Game.Game_status.IN_PLAY)

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

    '''
    if letter.upper() in current_game.word.upper():
        print ('in word')
    else: 
        print ('not in word ', current_game.word)
        current_game.message = 'TRY AGAIN!'
    '''

    letter_positions = []

    for i, l in enumerate (current_game.word):
        
        if letter.upper() == l.upper():
            letter_positions.append (i)

    print ('COUNT ' , letter_positions.count)

    if len(letter_positions) == 0:
        print (letter, ': not found')
        current_game.message = 'TRY AGAIN!'
    else:
        print ('positions', letter_positions)
        current_game.message = 'WELL DONE!'
        template_as_list = list(current_game.template)
        for replace_position in letter_positions:
            template_as_list [replace_position] = letter
        current_game.template = "".join(template_as_list) 

    if current_game.template.upper() == current_game.word.upper():
        current_game.game_status = current_game.Game_status["WON"] 
        current_game.message = 'WINNER!' 
        print ('Status: ', current_game.game_status)       
            


    


    # Update used_letters inside Game
    if letter not in current_game.used_letters:
        current_game.used_letters.append(letter)
    


    print("used_letters now in game:", current_game.used_letters)

    # Your hangman logic (stubbed to your existing code)
    # You probably want to use game.word instead of "ABACUS" eventually
    #current_game.template = template
    #current_game.message = template   # or a nicer message if you want

    # Save updated game back to session
    session["game"] = current_game.to_dict()

    return redirect(url_for("index"))


@app.route("/show_line", methods=["POST"])
def show_line():
    print('Hello')
    return redirect(url_for("index"))




@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")


# This is the root for the whole application
if __name__ == '__main__':
    app.run(debug=True)

"Relationship to main.py => Sends HTTP requests to, HTTP/HTTPS"
"Relationship from main.py - recieves feedback "
"for the user and displays it"



