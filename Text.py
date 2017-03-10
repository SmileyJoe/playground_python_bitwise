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
        floor_lower = ord('a')
        ceil_lower = ord('z')
        floor_upper = ord('A')
        return Text.__convert(text_input, floor_lower, ceil_lower, floor_lower - floor_upper)

    @staticmethod
    def lower(text_input):
        floor_lower = ord('a')
        floor_upper = ord('A')
        ceil_upper = ord('Z')
        return Text.__convert(text_input, floor_upper, ceil_upper, floor_upper - floor_lower)

    @staticmethod
    def __convert(text_input, floor, ceil, diff):
        text = []
        for char in text_input:
            char_value = ord(char)
            if char_value > floor and floor <= char_value <= ceil:
                text.append(chr(char_value - diff))
            else:
                text.append(char)
        return ''.join(text)
