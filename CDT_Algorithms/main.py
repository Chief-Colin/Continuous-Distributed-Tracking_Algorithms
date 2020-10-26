# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import heapq
import time
import csv as cv
import pandas as pd
from matplotlib import pyplot as plt
from array import array

def convert_dat_to_csv():
    temp = pd.read_csv('datastreams/outfile.csv')
    for items in temp:
        print(temp['sensor03'])
        #csv_writer.writerow(['sensor01', 'sensor02', 'sensor03', 'sensor04', 'sensor05', 'sensor06', 'sensor07', 'sensor08', 'sensor09', 'sensor10',
                             # 'sensor11', 'sensor12', 'sensor13', 'sensor14', 'sensor15', 'sensor16', 'sensor17', 'sensor18', 'sensor19', 'sensor20',
                             #'sensor21', 'sensor22', 'sensor23', 'sensor24', 'sensor25', 'sensor26', 'sensor27', 'sensor28', 'sensor29', 'sensor30',
                             #'sensor31', 'sensor32', 'sensor33', 'sensor34', 'sensor35', 'sensor36', 'sensor37', 'sensor38', 'sensor39', 'sensor40',
                             #'sensor41', 'sensor42', 'sensor43', 'sensor14', 'sensor45', 'sensor46', 'sensor47', 'sensor48', 'sensor49', 'sensor50',
                             #'sensor51', 'sensor52', 'sensor53', 'sensor54', 'sensor55', 'sensor56', 'sensor57', 'sensor58', 'sensor59', 'sensor60',
                             #'sensor61', 'sensor62', 'sensor63', 'sensor64', 'sensor65', 'sensor66', 'sensor67', 'sensor68', 'sensor69', 'sensor70',
                             #'sensor71', 'sensor72',
                             #])

        # for line in infile.read().splitlines():
            #csv_writer.writerow([line, prev])
            # prev = line
# receive data from the csv files using panda
temp = pd.read_csv('datastreams/geodata1.csv')
temp2 = pd.read_csv('datastreams/geodata2.csv')
df = pd.DataFrame(temp)
hitsPerTime2 = []
timePeriod2 = []
hitsPerTime = []
timePeriod = []

# implementation of the naive algorithm. In this algorithm the we compare to see if the previous messages sent to the
# coordinator is different from the new messages before it is sent to the coordinator. if it is not different, it is not
# sent and therefore not countered
def naiveAlgorithm():
    print(temp2)
    count = 1
    time = 0
    sensorK = 0
    totalNumberOfHits = 8

    for item in range(0, 999):
        numberOfHits = 0
        if int(temp['sensor01'][count]) != int(temp['sensor01'][count - 1]) and int(temp['sensor01'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp['sensor01'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp['sensor01'][count]) != int(
                temp['sensor04'][count - 1]) and int(temp['sensor01'][count]) != int(
                temp2['sensor01'][count - 1]) and int(temp['sensor01'][count]) != int(
                temp2['sensor02'][count - 1]) and int(temp['sensor01'][count]) != int(
                temp2['sensor03'][count - 1]) and int(temp['sensor01'][count]) != int(temp2['sensor04'][count - 1]):
                numberOfHits += 1
                totalNumberOfHits = totalNumberOfHits + 1

        if int(temp['sensor02'][count]) != int(temp['sensor01'][count - 1]) and int(temp['sensor02'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp['sensor02'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp['sensor04'][count]) != int(
                temp['sensor04'][count - 1]) and int(temp['sensor02'][count]) != int(
                temp2['sensor01'][count - 1]) and int(temp['sensor02'][count]) != int(
                temp2['sensor02'][count - 1]) and int(temp['sensor02'][count]) != int(
                temp2['sensor03'][count - 1]) and int(temp['sensor02'][count]) != int(temp2['sensor04'][count - 1]):
                numberOfHits += 1
                totalNumberOfHits = totalNumberOfHits + 1

        if int(temp['sensor03'][count]) != int(temp['sensor01'][count - 1]) and int(temp['sensor03'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp['sensor01'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp['sensor03'][count]) != int(
                temp['sensor04'][count - 1]) and int(temp['sensor03'][count]) != int(
                temp2['sensor01'][count - 1]) and int(temp['sensor03'][count]) != int(
                temp2['sensor02'][count - 1]) and int(temp['sensor03'][count]) != int(
                temp2['sensor03'][count - 1]) and int(temp['sensor03'][count]) != int(temp2['sensor04'][count - 1]):
                numberOfHits += 1
                totalNumberOfHits = totalNumberOfHits + 1

        if int(temp['sensor04'][count]) != int(temp['sensor01'][count - 1]) and int(temp['sensor04'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp['sensor04'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp['sensor04'][count]) != int(
                temp['sensor04'][count - 1]) and int(temp['sensor04'][count]) != int(
                temp2['sensor01'][count - 1]) and int(temp['sensor04'][count]) != int(
                temp2['sensor02'][count - 1]) and int(temp['sensor04'][count]) != int(
                temp2['sensor03'][count - 1]) and int(temp['sensor04'][count]) != int(temp2['sensor04'][count - 1]):
                numberOfHits += 1
                totalNumberOfHits = totalNumberOfHits + 1
        if int(temp2['sensor01'][count]) != int(temp['sensor01'][count - 1]) and int(temp2['sensor01'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp2['sensor01'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp2['sensor01'][count]) != int(
                temp['sensor04'][count - 1]) and int(temp2['sensor01'][count]) != int(
                temp['sensor01'][count - 1]) and int(temp2['sensor01'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp2['sensor01'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp2['sensor01'][count]) != int(temp['sensor04'][count - 1]):
                numberOfHits += 1
                totalNumberOfHits = totalNumberOfHits + 1
        if int(temp2['sensor02'][count]) != int(temp['sensor01'][count - 1]) and int(temp2['sensor02'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp2['sensor02'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp2['sensor04'][count]) != int(
                temp['sensor04'][count - 1]) and int(temp2['sensor02'][count]) != int(
                temp['sensor01'][count - 1]) and int(temp2['sensor02'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp2['sensor02'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp2['sensor02'][count]) != int(temp['sensor04'][count - 1]):
                numberOfHits += 1
                totalNumberOfHits = totalNumberOfHits + 1

        if int(temp2['sensor03'][count]) != int(temp['sensor01'][count - 1]) and int(temp2['sensor03'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp2['sensor01'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp2['sensor03'][count]) != int(
                temp['sensor04'][count - 1]) and int(temp2['sensor03'][count]) != int(
                temp['sensor01'][count - 1]) and int(temp2['sensor03'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp2['sensor03'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp2['sensor03'][count]) != int(temp['sensor04'][count - 1]):
                numberOfHits += 1
                totalNumberOfHits = totalNumberOfHits + 1

        if int(temp2['sensor04'][count]) != int(temp['sensor01'][count - 1]) and int(temp2['sensor04'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp2['sensor04'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp2['sensor04'][count]) != int(
                temp['sensor04'][count - 1]) and int(temp2['sensor04'][count]) != int(
                temp['sensor01'][count - 1]) and int(temp2['sensor04'][count]) != int(
                temp['sensor02'][count - 1]) and int(temp2['sensor04'][count]) != int(
                temp['sensor03'][count - 1]) and int(temp2['sensor04'][count]) != int(temp['sensor04'][count - 1]):
                numberOfHits += 1
                totalNumberOfHits = totalNumberOfHits + 1

        count = count + 1
        # print('--------------------')
        print(numberOfHits)
        # print(time)
        hitsPerTime.append(totalNumberOfHits)
        timePeriod.append(time)
        time += 1
        # print(count)


def simpleAlgorithm():
    #print(temp2)
    time2 = 0
    counts = 1
    cnt = 0
    numHits = 8
    i = 1

    for itm in range(0, 999):

        quant = [int(temp['sensor01'][cnt]), int(temp['sensor02'][cnt]), int(temp['sensor03'][cnt]),
                 int(temp['sensor04'][cnt]), int(temp2['sensor01'][cnt]), int(temp2['sensor02'][cnt]),
                 int(temp2['sensor03'][cnt]), int(temp2['sensor04'][cnt])]
        # print(quant)
        tenth = pd.DataFrame(quant)
        tempQuantile = tenth.quantile(.2)
        # print(tempQuantile)
        if i == 7:
            i = 0
        if int(temp['sensor01'][counts]) > int(tempQuantile):
            quant[i] = int(temp['sensor01'][counts])
            numHits += 1
            i = i + 1
            if i == 7:
                i = 0
        if int(temp['sensor02'][counts]) > int(tempQuantile):
            quant[i] = int(temp['sensor02'][counts])
            numHits += 1
            i = i + 1
            if i == 7:
                i = 0
        if int(temp['sensor03'][counts]) > int(tempQuantile):
            quant[i] = int(temp['sensor03'][counts])
            numHits += 1
            i = i + 1
            if i == 7:
                i = 0
        if int(temp['sensor04'][counts]) > int(tempQuantile):
            quant[i] = int(temp['sensor04'][counts])
            numHits += 1
            i = i + 1
            if i == 7:
                i = 0
        if int(temp2['sensor01'][counts]) > int(tempQuantile):
            quant[i] = int(temp2['sensor01'][counts])
            numHits += 1
            if i == 7:
                i = 0
        if int(temp2['sensor02'][counts]) > int(tempQuantile):
            quant[i] = int(temp2['sensor02'][counts])
            numHits += 1
            i = i + 1
            if i == 7:
                i = 0
        if int(temp2['sensor03'][counts]) > int(tempQuantile):
            quant[i] = int(temp2['sensor03'][counts])
            numHits += 1
            i = i + 1
            if i == 7:
                i = 0
        if int(temp2['sensor04'][counts]) > int(tempQuantile):
            quant[i] = int(temp2['sensor04'][counts])
            numHits += 1
            i = i + 1
            if i == 7:
                i = 0


        cnt = cnt + 1
        counts = counts + 1
        hitsPerTime2.append(numHits)
        timePeriod2.append(time2)
        time2 = time2 + 1
        print(numHits)

    print(tenth.quantile(.2))



def plotGraph():
    cnt = 0
    print(timePeriod)
    print(timePeriod2)
    plt.plot(timePeriod2, hitsPerTime2, label='Simple Algorithm')
    plt.plot(timePeriod, hitsPerTime, label='Naive Algorithm')
    plt.ylabel('Message Per Time t')
    plt.xlabel('Time t')
    plt.title('Top-k Algorithm')
    plt.legend()


    plt.show()
    for all in range(0, 1000):
        #if cnt < 1000:
            print(df['sensor01'].iloc[0])
            cnt = cnt + 1
            print(cnt)

    x = [1, 2, 3, 4, 5, 6]
    y = [1, 5, 3, 1, 2, 6]
    print(y)
    plt.plot(x, y)
    plt.show()



if __name__ == '__main__':
    #convert_dat_to_csv()
    naiveAlgorithm()
    simpleAlgorithm()
    plotGraph()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
