def used_letters_function(letter, used_letters):
       #This will make a list of used letters
       #Ensure all letters are to lower, white space removed etc
       #This currently has a bug: The list is not being appended. Rather,
       # it is being overwritten.
       used_letters.append(letter)
       return used_letters

def guessed_words_function(guessed_word, words_guessed):
       #This will make a list of previously guessed words
       return None

used_letters_function("F", ["D","G"])