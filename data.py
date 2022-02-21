import pandas as pd
import pickle
from tqdm import tqdm
def read_data(p):
    df = pd.read_excel(p, engine='openpyxl')
    ins = set(df['设备'].to_list())
    data = {}
    date = {}
    for n in tqdm(ins):
        items = set(df.loc[df['设备']==n,'信号点名称'].to_list())
        for m in items:
            name = n+'_'+m
            data[name] = df.loc[(df['设备']==n)&(df['信号点名称']==m),'采集值'].to_list()
            date[name] = df.loc[(df['设备']==n)&(df['信号点名称']==m),'智慧物联网关采集时间'].to_list()
    return data,date



def main():

    data, date = read_data('data/燎原配电站房(厂房).xlsx')
    with open('data/saved_data.pkl', 'wb') as f:
        pickle.dump(data, f)
    with open('data/saved_date.pkl', 'wb') as f:
        pickle.dump(date, f)
    return 0



if __name__ == '__main__':
    main()