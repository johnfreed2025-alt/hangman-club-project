from enum import Enum
from re import sub

"Purpose: Core game rules and state management"
"Implements hangman rules and game state management"
"Relationships to main.py - recieves the selected word "
"from main and provides feedback on the guess"
"Relationships to main.py - recieves the selected guess"
" letter from main and provides feedback on the guess"
"Uses for game operations (start, guess, win/loss)"

# game needs a game_id, a new one should be generated if one does not exist
# Added using the id() function. This will change with every time the programme
#is run, so need find a way to assign the id permenantly

class Game():

    class Game_status (Enum):
        IN_PLAY = 0
        WON = 1
        LOST = 2


    def __init__(self, player_name, word):
        
        self.player_name = player_name
        self.score = 10 #remaining attempts
        self.word = word
        self.template = self.__set_template(word)
        self.game_status = self.Game_status (0)
        self.game_id = id(self)

    def __set_template (self, word):
        template = sub('[a-z,A-Z]', '_', word)
        return template 
    
    def get_game_status(self):
        return self.game_status
    
    def set_game_status(self, game_status):
        self.game_status = self.Game_status (game_status)
        return 
    
    
#example declare and use class
#x = Game('Rick','Beaver Dam')
#print (x._create_template('Dolder')) #test private function cannot be run outside of class
#print (x.get_game_status() )
#print (x.score)
#print (x.player_name)
#print (x.game_status)
#print (x.template)
#x.set_game_status (2)
#print (x.game_status)
#print (x.game_ID)
#x.set_game_status (x.Game_status['WON'])
#
#print (x.game_id)


    
#def is_itwon():
    # uses the output from make_guess to work out if the game 
    # has been won or not and tells the main programme the status
    #return None

#def remaining_attempts(number):
    #number -= 1
    #return(number)

#def display_word():
    #return None
    
#def to_dict(self):
    # this function is to store the game progress into the 
    # persistence file so that it can be resumed later
    #return None

#def from_dict(data):
    # this function is to restore the game progress 
    # from the persistence file if the game is resumed later
    # return None
    






