# Bitwise Python Playground #

This repo is a playground for using bitwise operations for various
tasks. This will be continuely updated, some classes/functions will also be in the process of being converted to bitwise
operations.

## Bit ##

Basic bitwise operations used for settings by toggling
bits.

Eg.

```
setting = Bit()
setting.set(LOGGED_IN)

if setting.is_set(LOGGED_IN):
    pprint("Logged in")
else:
    pprint("Logged out")
```

## Text ##

Using bit operations for text manipulation.

### Duplicate Character ###

Uses bitwise operations to check if a character is duplicated
in a given string.

## Math ##

Using bitwise operations to perform basic arithmetic.