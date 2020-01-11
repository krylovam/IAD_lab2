import io
import matplotlib.pyplot as plt
import numpy as np
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
dictionary = {}
with io.open("estimations.txt", encoding='utf-8') as f:
    text = f.read()
    words = text.split("\n")
    for i in words:
        if len(i):
            word = i.split()
            dictionary[word[0]] = int(word[1])
positive_adjs = []
negative_adjs = []
frequency_positive = []
frequency_negative = []
with io.open("Frequency.txt",encoding='utf-8') as f:
    data = f.read().split('\n')
    words = []
    data_about_words = []
    for line in data:
        if len(positive_adjs) >= 5 and len(negative_adjs) >= 5:
            break
        components = line.split(":")
        if components:
            p = morph.parse(components[0])
            if p[0].tag.POS == 'ADJF':
                if dictionary[components[0]] > 0 and len(positive_adjs) <= 5:
                    positive_adjs.append(components)
                    frequency_positive.append(components[1].split()[0])
                if dictionary[components[0]] < 0 and len(negative_adjs) <= 5:
                    negative_adjs.append(components)
                    frequency_negative.append(components[1].split()[0])

with io.open("Adjectives.txt", 'w', encoding='utf-8')as f:
    f.write("Top-5 Positive:\n")
    for i in positive_adjs:
        f.write(i[0]+" "+ i[1]+"\n")
    f.write("Top-5 Negative:\n")
    for i in negative_adjs:
        f.write(i[0]+" "+i[1]+"\n")
# Graph
barWidth = 0.25
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
bars1 = [i for i in frequency_positive]
bars2 = [i for i in frequency_negative]
r1 = [i[0] for i in positive_adjs]
r2 = [i[0] for i in negative_adjs]
graph2 = ax1.bar(r2[::-1], bars2[::-1], width=barWidth, color = 'red')
graph1 = ax2.bar(r1[::-1], bars1[::-1], width=barWidth, color = 'green')
plt.show()
