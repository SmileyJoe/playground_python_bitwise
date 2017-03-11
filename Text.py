from pprint import pprint


class Text:

    LOWER_MIN = 0x0061
    LOWER_MAX = 0x007A
    HIGHER_MIN = 0x0041
    HIGHER_MAX = 0x005A
    DIFF = 0x0020

    @staticmethod
    def has_duplicate_char(text_input):
        text = text_input.lower()
        value = 0
        for char in text:
            number = 1 << (ord(char) - Text.LOWER_MIN)
            if value & number != 0:
                return True
            else:
                value |= number
        return False

    @staticmethod
    def upper(text_input):
        return Text.__convert(text_input, Text.LOWER_MIN, Text.LOWER_MAX, Text.DIFF)

    @staticmethod
    def lower(text_input):
        return Text.__convert(text_input, Text.HIGHER_MIN, Text.HIGHER_MAX, -Text.DIFF)

    @staticmethod
    def __convert(text_input, floor, ceil, diff):
        text = []
        for char in text_input:
            char_value = ord(char)
            if floor <= char_value <= ceil:
                text.append(chr(char_value - diff))
            else:
                text.append(char)
        return ''.join(text)
