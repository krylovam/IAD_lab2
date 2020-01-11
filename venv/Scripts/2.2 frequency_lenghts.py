from collections import Counter
import io
import re
def delete_trash(line):
    line = re.sub("#[ ]*[A-Za-zA-Яа-яё0-9]*", '', line) # тэги
    line = re.sub("@[ ]*[^ \n]*", '', line)
    line = re.sub(r'pic.*'," ",line)
    line = re.sub(r'https://*'," ",line)
    line = re.sub(r"[!.,@$%^&*()\-_=+\"№;?/`:«<>{}\[\]']"," ", line)
    return (line)
with io.open("file.txt", encoding='utf-8') as f:
    text = f.read()
    lines = text.split("\n")
    number = len(lines)
    lenghts = []
    for i in lines:
        if i:
            line = delete_trash(i[17:])
            if line:
                lenghts.append(len(line.split()))

lens = Counter(lenghts)
lens = lens.most_common()
with io.open("twits_length.txt", "w", encoding= 'utf-8') as f:
    for key in lens:
        f.write("{0}: {1} - {2}%\n".format(key[0], key[1], round(100 * key[1] / (number/2), 6)))

