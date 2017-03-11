from pprint import pprint
from Bit import Bit
from Text import Text
from Math import Math

pprint("Hello world")

LOGGED_IN = Bit.ONE
IS_PREMIUM = Bit.TWO
FULL_PROFILE = Bit.THREE

setting = Bit()

setting.set(LOGGED_IN)

setting.set(FULL_PROFILE)

setting.unset(LOGGED_IN)

if setting.is_set(LOGGED_IN):
    pprint("Logged in")
else:
    pprint("Logged out")

if setting.is_set(IS_PREMIUM):
    pprint("Premium")
else:
    pprint("Not Premium")

pprint("Has Duplicate: " + str(Text.has_duplicate_char("Cody")))
pprint("Upper: " + Text.upper("Cody-&cODy"))
pprint("Lower: " + Text.lower("Cody-&cODy"))

pprint("Add: " + str(Math.add(5, 5)))

pprint("End")

pprint(ord('a'))
pprint(ord('z'))
pprint(ord('A'))
pprint(ord('Z'))
