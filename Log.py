from pprint import pprint


class Log:

    @staticmethod
    def binary(key, value):
        pprint(key + ": " + "{0:b}".format(value))

    @staticmethod
    def log(key, value):
        pprint(key + ": " + str(value))
