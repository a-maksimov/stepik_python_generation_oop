from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length):
        self.length = length
        self.string = ''
        self._current_length = 0

    @abstractmethod
    def add(self, words):
        words = words.split()
        for word in words:
            test_length = self._current_length + len(word)
            if not test_length > self.length:
                self.string += word + ' '
                self._current_length += len(word + ' ')
            else:
                self.string = self.string.strip() + '\n' + word + ' '
                self._current_length = len(word + ' ')

    @abstractmethod
    def end(self):
        self._current_length = 0


class LeftParagraph(Paragraph):
    def __init__(self, length):
        super().__init__(length)

    def add(self, words):
        super().add(words)

    def end(self):
        super().end()
        print(self.string.rstrip())
        self.string = ''
        self._current_length = 0


class RightParagraph(Paragraph):
    def __init__(self, length):
        super().__init__(length)

    def add(self, words):
        super().add(words)

    def end(self):
        super().end()
        new_string = []
        for line in self.string.split('\n'):
            new_string.append(' ' * (self.length - len(line.rstrip())) + line.rstrip())
        print('\n'.join(new_string))
        self.string = ''


# TEST_4:
rightparagraph = RightParagraph(28)

rightparagraph.add('I will not regret the roses')
rightparagraph.add('Withered with a light spring')
rightparagraph.add('I love the grapes on the vines')
rightparagraph.add('Ripened in the hands under the mountain')
rightparagraph.end()

rightparagraph.add('The beauty of my green valley')
rightparagraph.add('Golden joy of autumn')
rightparagraph.add('oblong and transparent')
rightparagraph.add('Like the fingers of a young maiden')
rightparagraph.end()

# TEST_4:
#  I will not regret the roses
# Withered with a light spring
#     I love the grapes on the
#   vines Ripened in the hands
#           under the mountain
#       The beauty of my green
#  valley Golden joy of autumn
#  oblong and transparent Like
#       the fingers of a young
#                       maiden
