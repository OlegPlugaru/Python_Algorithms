"""
Given a string of words, reverse all the words

start = "This is the best"
finist = "best the is This"

"""

start = "This is the best"
# My solution 1
# f = start.split()
# f.reverse()

# start = ""
# start = " ".join(f)
# print(start)

# My solution 2
# start = " ".join(start.split()[::-1])
# print(start)


def reverse(s):
    length = len(s)
    spaces = [" "]
    words = []
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])

        i += 1
    words.reverse()
    return " ".join(words)


print(reverse(start))
