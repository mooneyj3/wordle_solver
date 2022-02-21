from wordle_dictionary import build_dictionary
import random

# Guess states:
#    0 : White (unguessed)
#    1 : Green
#    2 : Yellow
#    3 : Grey

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class WordleGame:

    def __init__(self, word_length=5, total_guesses=6):
        self.word_length = word_length
        self.total_guesses = total_guesses

        self.guess_array = []
        self.guesses = 0

        self.wd = build_dictionary(word_length)
        self.answer = self.wd[random.randint(1,len(self.wd)+1)]
    
    def is_word_correct_length(self, player_guess):
        return len(player_guess) == self.word_length
    
    def is_word_in_dictionary(self, player_guess):
        return player_guess in self.wd
            
    
    def guess_word(self, player_guess):
        # check if game is over
        if self.guesses >= self.total_guesses:
            return {-1, "Game Over"}
        
        # check if the word meets criteria
        if not self.is_word_correct_length(player_guess):
            return {-1, "Word needs to have %i characters" % (self.word_length)}
        if not self.is_word_in_dictionary:
            return {-1, "Invalid word"}
        
        # iterate through guessed word vs answer
        for i in range(self.word_length):
            ans_ltr = self.answer[i]
            gue_ltr = player_guess[i]

            

            # TODO: pick back up here.
            # Thought process -- leverage the 'a' in x and x.count() techniques to optimize how we solve this
            # start with the simple case (assuming no duplicate letters), then come back and handle duplicates
        

        

        

    




