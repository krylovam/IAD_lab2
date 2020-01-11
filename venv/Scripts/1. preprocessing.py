import io
import datetime
import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()
def delete_trash(line):
    line = re.sub("#[ ]*[A-Za-zA-Яа-яё0-9]*", '', line) # тэги
    line = re.sub("@[ ]*[^ \n]*", '', line)
    line = re.sub(r'pic.*'," ",line)
    line = re.sub(r'https://*'," ",line)
    line = re.sub(r"[!.,@$%^&*()\-_=+\"№;?/`:«<>{}\[\]']"," ", line)
    return (line)
def clean_up(raw_line):
    date_time = raw_line[:17]
    # дата и время
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M ")
    raw_line = delete_trash(raw_line)
    result_line = []
    result_line.append(date_time)
    raw_line = raw_line.lower().split()
    for word in raw_line:
        if re.search('[а-я]', word):
            p = morph.parse(word)[0]
            if p.tag.POS != "CONJ" and p.tag.POS != "PREP" and p.tag.POS != "PRCL":
                result_line.append(p.normal_form)
    return result_line

with io.open("file.txt", encoding='utf-8') as f:
    data = []
    lines = f.read()
    counter = 0
    for line in lines.split('\n'):
        if line:
            result  = clean_up(line)
            if len(result) > 1:
                data.append(result)
                counter += 1
                print(counter)
with io.open("file_result.txt",'w', encoding='utf-8') as f:
    for i in data:
        for word in i[1:]:
            f.write(word)
            f.write(" ")
        f.write("\n")
with io.open("result_with_time.txt",'w', encoding='utf-8') as f:
    for i in data:
        f.write(i[0].strftime("%H:%M %d-%m-%Y "))
        for word in i[1:]:
            f.write(word)
            f.write(" ")
        f.write("\n")

