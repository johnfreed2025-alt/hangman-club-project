def Make_guess(letter, word, guess_result):

        letter_found = False
                
        word_with_guessed_letters = enumerate(guess_result)
        enumerate(word)
                
        for i,x in enumerate(word):

                if letter == x:
                                
                        guess_result[i] = letter
                        letter_found = True

        if letter_found:
                return {
                "success": True,
                "message": "Good job genius",
                "word_progress": guess_result
                }
        
        else:
                return {
                "success": False,
                "message": "Bad guess you lemon",
                "word_progress": guess_result
                }
