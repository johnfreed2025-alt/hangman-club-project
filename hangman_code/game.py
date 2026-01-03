"Defines the class Game that holds details of the game and provides game specific functions"

# game needs a game_id, a new one should be generated if one does not exist
# Added using the id() function. This will change with every time the programme
#is run, so need find a way to assign the id permenantly

from enum import Enum
from re import sub

class Game:

    class Game_status(Enum): # RP: I have made a note of this 
        # in game_status_function
        NEW_GAME = 0
        IN_PLAY = 1
        WON = 2
        LOST = 3

    def __init__(
        self,
        game_name='', # I haven't used this elsewhere. Is it in app?
        word=[""], # will get word from word_selection via the start_
        #game function
        *,
        game_id = 1,
        current_score = 0,
        template=None,
        message='game message', # Used in play_game errors
        used_letters=[""],
        game_started=True,
        current_game_status=[],
        accepted_letters = [], # RP: used for app.py to display letters
        guess_result = [""], # Sucess, Failure
        attempts_remaining = 10,
        guessed_word = [""], # this is the word in current play with guessed 
        #letters
        words_guessed = [""], # this is if the player tried to guess a full
        #word rather than individual letters
        Start_Game_Selection = "", # will be click on New, Resume 
        # or Exit from the user. Guess this could need an enum?
        game_closed = False,
        cumulative_score = 0,
        number_of_games_played = 0,
        number_of_games_won = 0,
                ):
        
        self.game_id = id(self)              # This will produce a unique id 
        #But we need to use update_data ind data handling to store it
        #Straight away else is will keep changing
        self.__game_name = game_name
        self.score_keeping = current_score #I assumed this was some sort
        # of calculated overall score that feeds into cumulative score
        self.word = word
        self.message = message
        self.used_letter = used_letters if used_letters is not None else []
        self.game_status = current_game_status
        # if template is not provided, generate it from the word
        self.template = template if template is not None else self.__set_template(word)
        #---------------------------------------------------------------------
        #In terms of seperation of concerns, does the below if statement
        # below in the validate_inoput function?
        #------------------------------------------------------------------
        self.accepted_letters = (
                                accepted_letters
                                if accepted_letters is not None
                                else [chr(c) for c in range(ord("A"), ord("Z") + 1)]
                                )
        self.word_progress = guess_result
        self.guessed_words = guessed_word
        self.remaining_attempts = attempts_remaining
        self.cumulative_score = cumulative_score
        self.number_games_played = number_of_games_played
        self.number_games_won = number_of_games_won
        self.words_guessed = words_guessed
        
        # default game status is NEW_GAME
        #self.game_status = (
            #game_status if isinstance(game_status, Game.Game_status)
            #else Game.Game_status.NEW_GAME
#)

#----------------------------------------------------------------------------
# I have similar to the below logic in main. 
# I think it should belong in main as it is part of the flow?
#----------------------------------------------------------------------------
        if isinstance(current_game_status, Game.Game_status):
            self.game_status = current_game_status
        elif isinstance(current_game_status, int):
            self.game_status = Game.Game_status(current_game_status)
        else:
            self.game_status = Game.Game_status.NEW_GAME
        
    
        print ('Game returned by init: ', self, self.message)
#----------------------------------------------------------------------------
#Seperation of concerns? I think this belongs in start_game
#---------------------------------------------------------------------------
    def __set_template(self, word):
        template = sub('[a-zA-Z]', '_', word)
        return template

    # -- functions not required
    # RP: They are required but are now in the game_status_function
    def get_game_status(self):
        return self.game_status

    def set_game_status(self, game_status):
        self.game_status = game_status
        return

    def get_game_name(self):
        return self.__game_name 
    
    def set_game_name(self, game_name):
        self.__game_name = game_name
    # ---------- helpers for session storage ----------

    def to_dict(self):
        """Serialize the game to plain types (for session / JSON)."""
        return {
            "game_id": self.game_id,
            "game_name": self.get_game_name(),
            "score": self.score,
            "word": self.word,
            "template": self.template,
            "message": self.message,
            "used_letters": self.used_letters,
            "accepted_letters": self.accepted_letters,
            "game_status": self.game_status.value,  # store enum as int
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Game":
        """Rebuild a Game instance from a dict (e.g. from session)."""
        return cls(
            game_name=data.get("game_name",""),
            word=data["word"],
            game_id=data.get("game_id", 1),
            score=data.get("score", 10),
            template=data.get("template"),
            message=data.get("message"),
            used_letters=data.get("used_letters", []),  # ✅ default to []
            accepted_letters=data.get("accepted_letters", []),
            game_status=Game.Game_status(data.get("game_status", 0)),
        )
    






