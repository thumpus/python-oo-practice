"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """
    machine to find a random word from a designated file
    file must have one word per line
    example: random_word_finder = WordFinder("words.txt")
    """

    def __init__ (self, path):
        """initializes the word finder, populates it with the list of words"""
        self.words = []
        self.path = path
        file = open(self.path, "r")
        for line in file:
            self.words.append(line)
        file.close()
        

    def __repr__(self):
        return f"<Random Word Generator, generating words from {self.path}>"
    
    def getWord(self):
        return choice(self.words).replace("\n", "")

class SpecialWordFinder(WordFinder):
        """
        word finder that ignores lines starting with # or blank lines
        example: special_finder = SpecialWordFinder("words.txt")
        """
        def __init__(self, path):
            super().__init__(path)
        
        def getWordSpecial(self):
            word = choice(self.words).replace("\n", "")
            if word[0] == "#" or word == "":
                word = choice(self.words).replace("\n", "")
            return word
            