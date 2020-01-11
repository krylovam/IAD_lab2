import io
import datetime
import numpy as np
import matplotlib.pyplot as plt
swear_words_dictionary = []
with io.open("estimations.txt", encoding='utf-8') as f:
    text = f.read()
    text = text.split('\n')
    for line in text:
        word = line.split()
        if len(word) and int(word[1]) == -2:
            swear_words_dictionary.append(word[0])
twits_number  = 0
last_twits_number = 0
twits_number_in_time = []
time = []
counter = 0
last_counter = 0
with io.open("result_with_time.txt", encoding='utf-8') as f:
    text = f.read()
    text = text.split('\n')
    text = text[::-1]
    datetime_start = datetime.datetime.strptime(text[1][:17], "%H:%M %d-%m-%Y ")
    for twit in text:
        if len(twit)> 1:
            counter += 1
            curr_datetime = datetime.datetime.strptime(twit[:17], "%H:%M %d-%m-%Y ")
            if curr_datetime > datetime_start + datetime.timedelta(hours=1):
                twits_number_in_time.append((twits_number - last_twits_number)/(counter-last_counter))
                time.append(curr_datetime)
                datetime_start = curr_datetime
                last_twits_number = twits_number
                last_counter = counter
            words = twit.split()
            for word in words:
                if word in swear_words_dictionary:
                    twits_number += 1
x_pos = np.arange(len(time))
plt.plot(time , twits_number_in_time)

plt.show()


