from Log import Log


class Math:

    @staticmethod
    def add(x, y):
        while y != 0:
            temp = x & y
            x ^= y
            y = temp << 1
        return x
