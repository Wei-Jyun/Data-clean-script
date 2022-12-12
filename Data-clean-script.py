import pandas as pd
import numpy
import datetime as dt

def pointdata_cnt(date):
    lines = []
    with open('usr/Documents/documents_'+ date +'.TXT') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number not in range(1,6):
                lines.append(line)

    with open('usr/Documents/documents_'+ date +'.TXT', 'w') as file:
        file.writelines(lines)
    data = pd.read_csv('usr/Documents/documents.TXT', sep=',', header=None)
    data.columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o"]
    data = data.drop(['o'], axis = 1)
    # data['a'] = data['a'].apply(lambda x: x.strftime('%Y-%M-%D'))
    data['c'] = data['c'].astype('str')
    data['c'] = data['c'].str.strip().str.zfill(5)
    data['d'] = data['d'].astype('str')
    data['d'] = data['d'].str.strip().str.zfill(4)

    def dataclip_cnt(cnt_data, date):
        length = len(cnt_data)
        clip_count = (length // 5000) +1
        for i in range(0, clip_count):
            After_data = cnt_data.loc[5000*i: (5000*(i+1))-1]
            print(After_data)
            After_data.to_csv('usr/Documents/ Documents ' + str(date) + "-CNT-" + str(i+1) + ".txt", header = None, index = False)
    dataclip_cnt(data, date)

def pointdata_amt(date):
    lines = []
    with open('usr/Documents/documents_'+ date +'.TXT') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number not in range(1,6):
                lines.append(line)

    with open('usr/Documents/documents_'+ date +'.TXT', 'w') as file:
        file.writelines(lines)
    data = pd.read_csv('usr/Documents/documents.TXT', sep=',', header=None)
    data.columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p"]
    data = data.drop(['o'], axis = 1)
    data = data.drop(['p'], axis = 1)
    data['c'] = data['c'].astype('str')
    data['c'] = data['c'].str.strip().str.zfill(5)
    data['d'] = data['d'].astype('str')
    data['d'] = data['d'].str.strip().str.zfill(4)
    data[["e", "f", "g", "h", "i", "j", "k", "l", "m"]] = data[["e", "f", "g", "h", "i", "j", "k", "l", "m"]].astype('int')
    data[["e", "f", "g", "h", "i", "j", "k", "l", "m"]] = data[["e", "f", "g", "h", "i", "j", "k", "l", "m"]].astype('str')
    data[["e", "f", "g", "h", "i", "j", "k", "l", "m"]] = '+'+data[["e", "f", "g", "h", "i", "j", "k", "l", "m"]]
    def dataclip_cnt(cnt_data, date):
        length = len(cnt_data)
        clip_count = (length // 5000) +1
        for i in range(0, clip_count):
            After_data = cnt_data.loc[5000*i: (5000*(i+1))-1]
            print(After_data)
            After_data.to_csv('usr/Documents/ Documents ' + str(date) + "-AMT-" + str(i+1) + ".txt", header = None, index = False)
    dataclip_cnt(data, date)


pointdata_cnt('20221207')
pointdata_amt('20221207')
