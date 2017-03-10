from pprint import pprint


class Text:

    @staticmethod
    def has_duplicate_char(text_input):
        text = text_input.lower()
        base = ord('a')
        value = 0
        for char in text:
            number = 1 << (ord(char) - base)
            if value & number != 0:
                return True
            else:
                value |= number
        return False
