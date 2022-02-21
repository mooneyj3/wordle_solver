from wordle_dictionary import build_dictionary
import random

# Guess states:
WHITE = 0
GREEN = 1
YELLOW = 2
GREY = 3

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class WordleGame:

    def __init__(self, word_length=5, total_guesses=6):
        self.word_length = word_length
        self.total_guesses = total_guesses

        self.guess_array = {}
        self.guesses = 0

        self.wd = build_dictionary(word_length)
        self.answer = self.wd[random.randint(1,len(self.wd)+1)]

        self.alpha_dict = dict.fromkeys(ALPHABET, WHITE)
    
    def is_word_correct_length(self, player_guess):
        return len(player_guess) == self.word_length
    
    def is_word_in_dictionary(self, player_guess):
        return player_guess in self.wd
    
    def create_guess_result(self, player_guess):
        # create Guess dictionary to store reselts
        # Format: {0 : {ltr, STATE}}
        guess_result = {}
        for i in range(self.word_length):
            guess_result[i] = {player_guess[i] : WHITE}
        return guess_result
    
    def get_char_indices_from_str(self, ch_in, str_in):
        return [ i for i, ltr in enumerate(str_in) if ltr == ch_in ]
    
    def set_alpha_dict_state(self, ch, state):
        if self.alpha_dict[ch] == GREEN:
            return
        self.alpha_dict = state
        return

    def guess_word(self, player_guess):
        player_guess = player_guess.lower()

        # check if game is over
        if self.guesses >= self.total_guesses:
            return {-1, "Game Over"}
        self.guesses += 1
        
        # check if the word meets criteria
        if not self.is_word_correct_length(player_guess):
            return {-1, "Word needs to have %i characters" % (self.word_length)}
        if not self.is_word_in_dictionary:
            return {-1, "Invalid word"}

        guess_result = self.create_guess_result(player_guess)
        
        # iterate through guessed word vs answer
        for i in range(self.word_length):
            # ans_ltr = self.answer[i]
            gue_ltr = player_guess[i]

            # skip letter if it's already been handled with duplicates
            if guess_result[i][gue_ltr] != WHITE:
                continue

            ans_idxs = self.get_char_indices_from_str(gue_ltr, self.answer)
            gue_idxs = self.get_char_indices_from_str(gue_ltr, player_guess)

            # GREY : no matches
            if len(ans_idxs) == 0:
                self.set_alpha_dict_state(gue_ltr, GREY)
                for h in gue_idxs:
                    guess_result[h][gue_ltr] = GREY
                continue

            # GREEN : exact match
            if ans_idxs == gue_idxs:
                self.set_alpha_dict_state(gue_ltr, GREEN)
                for h in gue_idxs:
                    guess_result[h][gue_ltr] = GREEN
                continue

            # case 1: guess letters less than or equal to answer letters
            # in this case, we mark as many hits as are in the answer
            if len(gue_idxs) <= len(ans_idxs):
                for h in gue_idxs:
                    if h in ans_idxs: # exact position match found
                        guess_result[h][gue_ltr] = GREEN
                        self.set_alpha_dict_state(gue_ltr, GREEN)
                    else:
                        guess_result[h][gue_ltr] = YELLOW
                        self.set_alpha_dict_state(gue_ltr, YELLOW)
                continue

            # case 2: more guess letters than answer letters
            # in this case the first hits are marked, and subsequent hits are greyed
            if len(gue_idxs) > len(ans_idxs):
                unmarked_ltrs = len(ans_idxs)

                # find green letters first
                for h in gue_idxs:
                    if unmarked_ltrs == 0:
                        break
                    if h in ans_idxs:
                        guess_result[h][gue_ltr] = GREEN
                        self.set_alpha_dict_state(gue_ltr, GREEN)
                        unmarked_ltrs -= 1

                # find yellow letters
                for h in gue_idxs:
                    if unmarked_ltrs == 0: 
                        break
                    if h in ans_idxs: # skip greens
                        continue
                    guess_result[h][gue_ltr] = YELLOW
                    self.set_alpha_dict_state(gue_ltr, YELLOW)
                    unmarked_ltrs -= 1
        
        # add the guess to the answer array and return
        self.guess_array[self.guesses] = guess_result





