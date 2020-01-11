import io
dictionary = {}

with io.open("words.txt", encoding='utf-8') as f:
    text = f.read()
    words = text.split("\n")
    for i in words:
        word = i.split()
        if len(word) > 1:
            dictionary[word[0]] = int(word[1])
        elif len(word) == 1:
            dictionary[word[0]] = 0
with io.open("estimations.txt", "w", encoding='utf-8') as f:
    for key in dictionary.keys():
        f.write(key + " " + str(dictionary[key]) + "\n")




