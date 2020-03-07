class UnscrambleMe:
    def __init__(self, puzzle):
        self.puzzle = set(puzzle)
        self.dict_words = set()
        
        # Populate the dict_words
        with open('/usr/share/dict/words', 'r') as file:
            source = file.readlines()
            for word in source:
                word = word.strip().lower()
                self.dict_words.add(word)

    def permutations(self, word, step, perm_words=None):
        '''Acknowledgement: s/o to my friend Noah Krause for showing me this permutation implementation'''
        if perm_words is None:
            perm_words = set()
        if step == len(word) - 1:
            perm_words.add(''.join(word))
        for i in range(step, len(word)):
            word[step], word[i] = word[i], word[step] 
            self.permutations(word, step + 1, perm_words) 
            word[step], word[i] = word[i], word[step]
        return perm_words


    def unscramble(self):
        unjumbled_words = set()
        for puzzle_word in self.puzzle:
            word_permutations = self.permutations(list(puzzle_word), 0)
            for word in word_permutations:
                if word in self.dict_words:
                    print(f'{puzzle_word} ended up being {word}')
                    unjumbled_words.add(word)
                    break
        print(f'Set of unjumbled words: {unjumbled_words}')
        return unjumbled_words

if __name__ == "__main__":
    fix_words = ['laisa', 'laurr', 'bureek', 'prouot']
    t1 = UnscrambleMe(fix_words)
    t1.unscramble() 

