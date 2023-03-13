"""
Given a string, are all characters unique?
should give a True or False return

Uses python built in structures
"""

s = "Hello world"

# def unique(string):
#     string = string.replace(' ', '')
#     return len(set(string)) == len(string)

# print(unique(s))

def unique(string):
    string = string.replace(" ", '')
    characters = set()

    for letter in string:
        if letter in characters:
            return False
        else: 
            characters.add(letter)
    return True

print(unique(s))
