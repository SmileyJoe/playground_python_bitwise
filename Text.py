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

    @staticmethod
    def upper(text_input):
        upper_text = []
        floor_lower = ord('a')
        ceil_lower = ord('z')
        floor_upper = ord('A')
        diff = floor_lower - floor_upper
        for char in text_input:
            char_value = ord(char)
            if char_value > floor_lower and floor_lower <= char_value <= ceil_lower:
                upper_text.append(chr(char_value-diff))
            else:
                upper_text.append(char)
        return ''.join(upper_text)
