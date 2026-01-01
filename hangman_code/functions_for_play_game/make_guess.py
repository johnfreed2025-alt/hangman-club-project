def Make_guess(letter, word, guessed_word):

        letter_found = False
                
        word_with_guessed_letters = list(guessed_word)
                
        for i,x in enumerate(word):

                if letter == x:
                                
                        word_with_guessed_letters [i] = letter
                        letter_found = True

        if letter_found:
                return {
                "success": True,
                "message": "Good job genius",
                "word_progress": word_with_guessed_letters
                }
        
        else:
                return {
                "success": False,
                "message": "Bad guess you lemon",
                "word_progress": word_with_guessed_letters
                }
