"Defines the class Game that holds details of the game and provides game specific functions"

# game needs a game_id, a new one should be generated if one does not exist
# Added using the id() function. This will change with every time the programme
#is run, so need find a way to assign the id permenantly

from enum import Enum
from re import sub

class Game:

    class Game_status(Enum):
        NEW_GAME = 0
        IN_PLAY = 1
        WON = 2
        LOST = 3

    def __init__(
        self,
        game_name='',
        word='Word 1',
        *,
        game_id=1,
        score=10,
        template=None,
        message='game message',
        used_letters=None,
        game_started=True,
        game_status=None,
        accepted_letters = None

    ):
        self.game_id = game_id              # always 1 for now
        self.__game_name = game_name
        self.score = score                  # remaining attempts
        self.word = word
        self.message = message
        self.used_letters = used_letters if used_letters is not None else []
        self.game_started = game_started
        # if template is not provided, generate it from the word
        self.template = template if template is not None else self.__set_template(word)
        self.accepted_letters = (
                                accepted_letters
                                if accepted_letters is not None
                                else [chr(c) for c in range(ord("A"), ord("Z") + 1)]
                                )
        # default game status is NEW_GAME
        #self.game_status = (
            #game_status if isinstance(game_status, Game.Game_status)
            #else Game.Game_status.NEW_GAME
        #)
        if isinstance(game_status, Game.Game_status):
            self.game_status = game_status
        elif isinstance(game_status, int):
            self.game_status = Game.Game_status(game_status)
        else:
            self.game_status = Game.Game_status.NEW_GAME
        
    
        print ('Game returned by init: ', self, self.message)

    def __set_template(self, word):
        template = sub('[a-zA-Z]', '_', word)
        return template

    # -- functions not required
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
    






