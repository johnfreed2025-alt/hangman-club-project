
def Validate_input(letter, used_letters):

        """This is a function to validate that the user has made a valid guess
        For example, have not tried a number or special character"""

        for i in used_letters:
            if i == letter:
                raise ValueError("This letter has been previously guessed")

        if not isinstance(letter, str):
                raise TypeError("letter must be alphabetic")

        if len(letter) != 1:
                raise ValueError("must be one character")

        if not letter.isalpha():
                raise ValueError("must be alphabetic")
        
        else:
                return True
        

