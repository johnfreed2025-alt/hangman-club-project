# User playing hangman in their browser"
# Relationship to routes_py => Sends HTTP requests to, HTTP/HTTPS"
# Relationship from routes_py - recieves feedback for the user and displays it"

from flask import Flask, request, redirect, url_for, render_template, session
#from string import ascii_uppercase
# above was imported but unused
import hangman_code.main
from  hangman_code.game import Game

app = Flask(__name__)
app.secret_key = "super-secret-key-change-this"

@app.route("/", methods=["GET"])
def index():
    message = session.get("message", "")
    word_template = session.get("template", "")
    disabled_letters = session.get("disabled_letters", [])

    # Letters used in the template – uppercase A–Z
    letters = [chr(c) for c in range(ord("A"), ord("Z") + 1)]

    # Debug: see what disabled_letters we’re sending to the page
    print("Rendering index with disabled_letters:", disabled_letters)

    return render_template(
        "index.html",
        message=message,
        template=word_template,
        letters=letters,
        disabled_letters=disabled_letters,
    )


@app.route("/guess", methods=["POST"])
def guess():
    # Get the letter from the form
    letter = request.form.get("letter")
    if not letter:
        print("⚠️ /guess called without 'letter'. FORM DATA:", request.form)
        return redirect(url_for("index"))

    # Normalize to uppercase (your letters list is A–Z)
    letter = letter.upper()
    print("Guessed:", letter)

    # Read current disabled letters from the session, add this one
    disabled = set(session.get("disabled_letters", []))
    disabled.add(letter)
    session["disabled_letters"] = list(disabled)

    # Your hangman logic
    template = hangman_code.main.guess(letter, "ABACUS")
    session["message"] = template

    # Debug: see what is now in the session
    print("Disabled letters now:", session["disabled_letters"])

    return redirect(url_for("index"))

@app.route("/new_game", methods=["POST"])
def new_game():
    print('new game button pressed')
    this_game = Game('Rick', 'todays word')
    print(this_game.template)

    # ✅ keep key names consistent with index()
    session["template"] = this_game.template

    # ✅ reset everything for a fresh game
    session["message"] = ""              # or "New game started!"
    session["disabled_letters"] = []     # re-enable all buttons

    return redirect(url_for("index"))



@app.route("/C", methods=["POST"])
def C():
    session["c_disabled"] = True
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
"Relationship to main.py => Sends HTTP requests to, HTTP/HTTPS"
"Relationship from main.py - recieves feedback "
"for the user and displays it"



