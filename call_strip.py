class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        for _ in range(len(string)):
            for char in self.chars:
                string = string.strip(char)

        return string


strip = Strip('.,+-')

print(strip('     --++beegeek++--'))
print(strip('-bee...geek-'))
print(strip('-+,.b-e-e-g-e-e-k-+,.'))