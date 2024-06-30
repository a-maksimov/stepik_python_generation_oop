class TextHandler:
    def __init__(self):
        self.words = []
        self.max_len = None
        self.min_len = None

    def add_words(self, text):
        self.words.extend(text.split())
        if self.max_len is None:
            self.max_len = len(max(self.words, key=len))
        if self.min_len is None:
            self.min_len = len(min(self.words, key=len))
        if self.max_len < len(max(self.words, key=len)):
            self.max_len = len(max(self.words, key=len))
        if self.min_len > len(min(self.words, key=len)):
            self.min_len = len(min(self.words, key=len))

    def get_shortest_words(self):
        return [word for word in self.words if len(word) == self.min_len]

    def get_longest_words(self):
        return [word for word in self.words if len(word) == self.max_len]


texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())