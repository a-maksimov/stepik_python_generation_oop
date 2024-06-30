class Wordplay:
    def __init__(self, words=None):
        if words is None:
            self.words = []
        else:
            self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only(self, *letters):
        return [word for word in self.words if set(word).issubset(letters)]

    def avoid(self, *letters):
        return [word for word in self.words if set(word).isdisjoint(letters)]


wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word('bee')
wordplay.add_word('geek')
print(wordplay.words)
