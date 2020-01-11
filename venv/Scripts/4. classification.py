import io
import matplotlib.pyplot as plt
import numpy as np
dictionary = {}
classification = []
with io.open("estimations.txt", encoding='utf-8') as f:
    text = f.read()
    words = text.split("\n")
    for i in words:
        if len(i):
            word = i.split()
            dictionary[word[0]] = int(word[1])

with io.open("result_with_time.txt", encoding='utf-8') as f:
    text = f.read()
    text = text.split("\n")
    # first rule
with io.open("twit_estimation1.txt",'w',encoding = 'utf-8') as f:
    count_bad = 0
    count_good = 0
    count_neutral =0
    for line in text:
        line = line.split()
        if len(line) < 3:
            break
        time = line[:2]
        line = line[2:]
        tweet_mark = 0
        for word in line:
            if dictionary.get(word):
                if dictionary[word] < 0:
                    tweet_mark -= 1
                else:
                    tweet_mark += dictionary[word]
        if tweet_mark < 0:
            count_bad += 1
            f.write(time[0] + " " + time[1] + " 2 ")
        elif tweet_mark > 2:
            count_good += 1
            f.write(time[0] + " " + time[1] + " 1 ")
        else:
            count_neutral += 1
            f.write(time[0] + " " + time[1] + " 0 ")
        for i in line:
            f.write(i + " ")
        f.write("\n")
    classification.append([count_good,count_neutral,count_bad])

# second rule
with io.open("twit_estimation2.txt",'w',encoding = 'utf-8') as f:
    count_bad = 0
    count_neutral = 0
    count_good = 0
    for line in text:
        line = line.split()
        if len(line) < 3:
            break
        time = line[:2]
        line = line[2:]
        good_words = 0
        bad_words = 0
        neutral_words = 0
        tweet_mark = 0
        for word in line:
            if dictionary.get(word):
                if dictionary[word] > 0:
                    good_words += 1
                else:
                    bad_words += 1
            else:
                neutral_words += 1
        if max(good_words, bad_words,neutral_words) == good_words:
            count_good += 1
            f.write(time[0] + " " + time[1] + " 1 ")
        elif max(good_words, neutral_words, bad_words) == bad_words:
            count_bad += 1
            f.write(time[0] + " " + time[1] + " 2 ")
        elif max(good_words, neutral_words, bad_words) == neutral_words:
            count_neutral += 1
            f.write(time[0] + " " + time[1] + " 0 ")
        for i in line:
            f.write(i + " ")
        f.write("\n")
    classification.append([count_good,count_neutral,count_bad])

# third rule
with io.open("twit_estimation3.txt",'w',encoding = 'utf-8') as f:
    count_bad = 0
    count_neutral = 0
    count_good = 0
    for line in text:
        line = line.split()
        if len(line) < 3:
            break
        time = line[:2]
        line = line[2:]
        good_words = 0
        bad_words = 0
        neutral_words = 0
        tweet_mark = 0
        for word in line:
            if dictionary.get(word):
                if dictionary[word] > 0:
                    good_words += 1
                else:
                    bad_words += 1
            else:
                neutral_words += 1
        try:
            if bad_words/len(line) > 0.1:
                count_bad += 1
                f.write(time[0] + " " + time[1] + " 2 ")
            elif good_words/len(line) > 0.2:
                count_good += 1
                f.write(time[0] + " " + time[1] + " 1 ")
            else:
                count_neutral += 1
                f.write(time[0] + " " + time[1] + " 0 ")
            for i in line:
                f.write(i + " ")
            f.write("\n")
        except ZeroDivisionError:
            print("zero line")
    classification.append([count_good,count_neutral,count_bad])

# forth rule
with io.open("twit_estimation4.txt",'w',encoding = 'utf-8') as f:
    count_bad = 0
    count_neutral = 0
    count_good = 0
    for line in text:
        line = line.split()
        if len(line) < 3:
            break
        time = line[:2]
        line = line[2:]
        good_words = 0
        bad_words = 0
        neutral_words = 0
        tweet_mark = 0
        for word in line:
            if dictionary.get(word):
                if dictionary[word] > 0:
                    good_words += 1
                else:
                    bad_words += 1
            else:
                neutral_words += 1
        if  bad_words > 1:
            count_bad += 1
            f.write(time[0] + " " + time[1] + " 2 ")
        elif good_words > 1 :
            count_good += 1
            f.write(time[0] + " " + time[1] + " 1 ")
        else:
            count_neutral += 1
            f.write(time[0] + " " + time[1] + " 0 ")
        for i in line:
            f.write(i + " ")
        f.write("\n")
    classification.append([count_good,count_neutral,count_bad])

#make plot
barWidth = 0.25
bars1 = [i[0] for i in classification]
bars2 = [i[1] for i in classification]
bars3 = [i[2] for i in classification]
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
plt.bar(r1, bars1, color='lightseagreen', width=barWidth, edgecolor='white', label='good' )
plt.bar(r2, bars2, color='lightblue', width=barWidth, edgecolor='white', label='neutral')
plt.bar(r3, bars3, color='orangered', width=barWidth, edgecolor='white', label ='bad')
plt.xlabel('classification', fontweight='bold')
plt.xticks([r+ barWidth for r in range(len(bars1))], ['first rule', 'second rule', 'third rule', 'forth rule'])
plt.legend()
plt.show()

with io.open("classifications.txt", "w", encoding='utf-8') as f:
    for i in range(4):
        f.write("\nRule №"+str(i+1)+"\n")
        f.write("Good - {0} - {1}%\n"
                "Bad - {2} - {3}%\n"
                "Neutral - {4} - {5}%\n".format(
            classification[i][0],round(100*classification[i][0]/len(text),3),
        classification[i][2],round(100*classification[i][2]/len(text),3),
        classification[i][1],round(100*classification[i][1]/len(text),3)))

