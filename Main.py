from pprint import pprint
from Bit import Bit
from Text import Text

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
pprint(ord('a') - ord('A'))
