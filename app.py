# User playing hangman in their browser"
# Relationship to routes_py => Sends HTTP requests to, HTTP/HTTPS"
# Relationship from routes_py - recieves feedback for the user and displays it"

from flask import Flask, request, redirect, url_for, render_template, session
from hangman_code.play_game_functions import load_game
from hangman_code.play_game_functions import play_game
import string


app = Flask(__name__)
app.secret_key = "super-secret-key-change-this"


# This is the home page. It has a selection of new game, resume game,
# Factory reset or exit game.
#The Start_game_selection function will return the game object with the correct
# Data in it for its selection
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selection = request.form.get("action")
        print(f"This is the selection : {selection}")
        session["game"] = load_game(selection)
        print(f"This is the game input from Start Game Selection : {session["game"]}")
        return render_template("playing_game.html", game=session["game"],alphabet=string.ascii_uppercase)
    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():

    current_game = session["game"]
    # Get the letter from the form
    letter = request.form.get("letter")
        # Get the letter from the form
    if not letter:
        print("⚠️ /guess called without 'letter'. FORM DATA:", request.form)
        return redirect(url_for("index"))
    play_game(current_game, letter)

    #SAVING FOR LATER
    #if not letter:
        #print("⚠️ /guess called without 'letter'. FORM DATA:", request.form)
        #return redirect(url_for("index"))

    # TO BE DONE BY VALIDATE INPUT
    # Normalize to uppercase (your letters list is A–Z)
    #letter = letter.upper()
    #print("Guessed:", letter)

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
    #session["game"] = current_game.to_dict()

    return redirect(url_for("index"))


@app.route("/name_game", methods=["POST"])
def name_game():
    
    current_game = session["game"]

    # 1. Read the name from the form
    game_name = request.form.get("game_name").strip()

    # 2. Add the game name to the local game object

    current_game["game_name"] = game_name

    #3. Update the current_game_status to in play
    current_game["current_game_status"] = 1

    # 4. Store updated object back into session
    session["game"] = current_game
    print ('in name game:', session["game"]["game_name"])

    # 5. Back to the main page
    return render_template("playing_game.html", game=session["game"])


@app.route("/reset", methods=["POST"])
def reset():
    return redirect("/")

@app.route("/show_line", methods=["POST"])
def show_line():
    print('Hello')
    return redirect(url_for("index"))

@app.route("/closed", methods=["POST"])
def closed():
    request.form.get("action")
    return render_template("closed.html")

if __name__ == '__main__':
    app.run(debug=True)



