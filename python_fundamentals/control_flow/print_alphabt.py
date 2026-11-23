#!/usr/bin/env python3
alphabet = ""
for letter in range(97, 123):
    if chr(letter) not in ("q", "e"):
        alphabet += chr(letter)
print(alphabet)
