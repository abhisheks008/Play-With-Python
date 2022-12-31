import json


class MorseCode:
    def __init__(self):
        self.text2morse = json.load(open('text2morse.json'))
        self.morse2text = json.load(open('morse2text.json'))

    def encrypt_word(self, word):
        morse = list()
        for letter in word:
            try:
                data = self.text2morse[letter]
            except ValueError:
                return '/*Error*/'
            except KeyError:
                return '/*Error*/'
            morse.append(data)
        return ' '.join(morse)

    def decrypt_word(self, word):
        letters = word.split()
        text = list()
        for letter in letters:
            try:
                data = self.morse2text[letter]
            except ValueError:
                return '/*Error*/'
            except KeyError:
                return '/*Error*/'
            text.append(data)
        return ''.join(text)

    def encryptor(self, text):
        if ' ' in text:
            words = text.split()
            morse = list()
            for word in words:
                try:
                    data = self.encrypt_word(word)
                except ValueError:
                    return '/*Error*/'
                except KeyError:
                    return '/*Error*/'
                morse.append(data)
            return '  '.join(morse)
        return self.encrypt_word(text)

    def decrypter(self, morse):
        if '  ' in morse:
            words = morse.split('  ')
            text = list()
            for word in words:
                try:
                    data = self.decrypt_word(word)
                except ValueError:
                    return '/*Error*/'
                except KeyError:
                    return '/*Error*/'
                text.append(data)
            return ' '.join(text)
        return self.decrypt_word(morse)
