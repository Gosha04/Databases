def censor(string):
    curses = ["fuck", "shit", "bitch"]
    string = string.lower()
    for word in curses:
        string = string.replace(word.lower(), '****')

    return string

lyrics = input()
censor_lyrics = censor(lyrics)
print(censor_lyrics)