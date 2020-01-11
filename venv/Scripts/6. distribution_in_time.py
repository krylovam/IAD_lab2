import datetime
import io
import matplotlib.pyplot as plt
import numpy as np

for rool in range(1,5):
    with io.open('twit_estimation{0}.txt'.format(rool), encoding='utf-8') as f:
        text = f.read()
        sorted_by_time = []
        for i in text.split('\n')[:len(text)-1]:
            if i:
                time = datetime.datetime.strptime(i[:17], "%H:%M %d-%m-%Y ")
                mark = int(i[17])
                sorted_by_time.append([time, mark])
    sorted_by_time = sorted_by_time[::-1]
    time_start = sorted_by_time[0][0]
    time_end = time_start+ datetime.timedelta(minutes=15)
    iterator = 0
    with io.open('hours rool#{0}.txt'.format(rool), 'w', encoding='utf-8') as f:
        good = 0
        neutral = 0
        negative = 0
        list_good = []
        list_bad = []
        list_neutral = []
        count = []
        time = []
        while time_end < sorted_by_time[-1][0]:
            while sorted_by_time[iterator][0] < time_end:
                if sorted_by_time[iterator][1] == 1:
                    good += 1
                elif sorted_by_time[iterator][1] == 0:
                    neutral += 1
                else:
                    negative += 1
                iterator += 1
            number = good + negative + neutral
            if number:
                f.write(time_start.strftime('%H:%M %d-%m-%Y ') + time_end.strftime('-%H:%M %d-%m-%Y:'))
                f.write(" {0} {1}/{2}/{3}\n".format(number,round(good/number,3), round(neutral/number,3),
                                                    round(negative/number,3)))
                list_good.append(good/number)
                list_bad.append(negative/number)
                list_neutral.append(neutral/number)
                count.append(number)
                time.append(time_end)
            time_end = time_end + datetime.timedelta(minutes=10)
    # graph

    fig,(ax1,ax2) = plt.subplots(2,1, figsize=(27,6))
    x = [time[i] for i in range(0, len(time), 5)]
    x_pos = np.arange(len(x))
    good_graph = [list_good[i] for i in range(0,len(list_good),5)]
    neutral_graph = [list_neutral[i] for i in range(0,len(list_neutral),5)]
    negative_graph = [list_bad[i] for i in range(0,len(list_bad),5)]
    ax1.plot(x_pos, good_graph, color='green',linewidth=1, markersize=7,label='N_pos')
    ax1.plot(x_pos, neutral_graph, color='blue',linewidth=1, markersize=7,label='N_neu')
    ax1.plot(x_pos, negative_graph, color='red',linewidth=1, markersize=7,label='N_neg')
    ax1.set_xticks([])
    ax1.grid(True)
    ax1.legend()
    count_graph = [count[i] for i in range(0, len(count), 5)]
    ax2.stem(x_pos, count_graph)
    ax1.set_ylabel('Fraction')
    x_pos = [x_pos[i] for i in range(0,len(x_pos), 5)]
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels([x[i].strftime('%H:%M %d.%m') for i in range(0, len(x),5)])
    ax2.grid(True)
    ax2.set_ylabel('Number of twits')
    plt.show()
    fig.savefig('Time distribution rool#{0}.png'.format(rool))