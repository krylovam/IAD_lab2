from collections import Counter
import io
with io.open("file_result.txt", encoding='utf-8') as f:
    text = f.read()
    lines = text.split("\n")
    number = len(lines)
    text = text.split()
c = Counter(text)
c = c.most_common()
with io.open("Frequency.txt", 'w', encoding = 'utf-8') as f:
    f.write("<word>:<count> - <count/number of twits> - <count/numbers of wortds>\n")
    for key in c:
        f.write("{0}: {1} - {2}% - {3}%\n".format(key[0],key[1],
                                                  round(100*key[1]/number,4),round(100*key[1]/len(text),4)))


