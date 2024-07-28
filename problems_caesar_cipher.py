import string


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encode(self, text, shift=None):
        if shift is None:
            shift = self.shift
        symbols = [',', '.', '!', '"']
        text_coded_list = []
        text = text.split()
        word_coded = ''
        for word in text:
            word_original = word
            for symbol in symbols:
                word_stripped = word.strip(symbol)
                word = word_stripped
            for c in word_original:
                if c in string.ascii_lowercase:
                    char_ord = string.ascii_lowercase.find(c)
                    if char_ord + shift < len(string.ascii_lowercase):
                        word_coded += string.ascii_lowercase[char_ord + shift]
                    else:
                        word_coded += string.ascii_lowercase[char_ord + shift - len(string.ascii_lowercase)]
                elif c in string.ascii_uppercase:
                    char_ord = string.ascii_uppercase.find(c)
                    if char_ord + shift < len(string.ascii_uppercase):
                        word_coded += string.ascii_uppercase[char_ord + shift]
                    else:
                        word_coded += string.ascii_uppercase[char_ord + shift - len(string.ascii_uppercase)]
                else:
                    word_coded += c
            text_coded_list.append(word_coded)
            word_coded = ''
        text_coded = ' '.join(text_coded_list)
        return text_coded

    def decode(self, text):
        return self.encode(text, -self.shift)


cipher = CaesarCipher(5)
print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek
