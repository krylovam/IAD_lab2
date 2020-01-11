import io
import math
import operator
dictionary = {}
classification = []
with io.open("estimations.txt", encoding='utf-8') as f:
    text = f.read()
    words = text.split("\n")
    for i in words:
        if len(i):
            word = i.split()
            if word[1] == '-2':
                word[1] = '-1'
            dictionary[word[0]] = [int(word[1]),0,0,0]
for rool in range(1, 5):
    with io.open("twit_estimation{0}.txt".format(rool), encoding='utf-8') as f:
        real_estimation = {}
        text = f.read()
        text = text.split('\n')

        for line in text:
            line = line.split()
            if len(line) < 2:
                break
            mark = int(line[2])
            if mark == 2:
                mark = -1
            for word in line[3:]:
                if dictionary.get(word):
                    dictionary[word] = [dictionary.get(word)[0], dictionary.get(word)[1] + mark, dictionary.get(word)[2]+1,0]
        dictionary_result = {}
        for key in dictionary.keys():
            if dictionary.get(key)[2] > 2:
                dictionary_result[key] = [dictionary.get(key)[0], dictionary.get(key)[1], dictionary.get(key)[2],
                                   dictionary.get(key)[1] / dictionary.get(key)[2]]
                print(key, dictionary_result.get(key))

        sorted_dict = sorted(dictionary_result.items(), key=lambda kv: abs(kv[1][3]-kv[1][0]))
        e = 0.4
        accuracy = 0
        for i in sorted_dict:
            if abs(i[1][3] - i[1][0]) < e:
                accuracy +=1
        print(sorted_dict)
    with io.open("estimation_check rool#{0}".format(rool), "w", encoding ='utf-8') as f:
        f.write("Top-5 Closest:\n")
        for i in range(5):
            f.write(sorted_dict[i][0] + " "+str(sorted_dict[i][1][0])+" "+ str(round(sorted_dict[i][1][3],2))+"\n")
        f.write("\nTop-5 Furthest:\n")
        for i in range(1,6):
            f.write(sorted_dict[-i][0] +" "+ str(sorted_dict[-i][1][0]) +"  "+str(round(sorted_dict[-i][1][3], 2)) + "\n")
        f.write("Estimation accuracy: "+str(round(100*accuracy/len(sorted_dict),2))+"%\n")



