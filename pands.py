import pandas as pd
import datetime
import numpy as np
import csv


if __name__=="__main__":
    i=8
    total_dates=23
    today=datetime.datetime.today()

    correlation_datas=[[[0 for a in range(350)] for b in range(350)] for c in range(23)]
    standard_deviation=[[0 for i in range(350)] for j in range(350)]
    order_of_dates=0
    while(order_of_dates<total_dates):

        target_date= today - datetime.timedelta(i+order_of_dates)
        iter_date=target_date.strftime("20%y%m%d")

        print(iter_date)
        file_location='C:\\Users\\MINJUN KWAK\\Documents\\github\\stock_correlation_moniotring\\last price_v2_'+iter_date+'.xlsm'
        xl = pd.ExcelFile(file_location)
        # print(xl.sheet_names)

        df = xl.parse("CORR")

        print(df.iloc[3,3])
        for a in range(350):
            for b in range(350):
                correlation_datas[order_of_dates][a][b]=df.iloc[a+3,b+3]


        # print(order_of_dates,correlation_datas[order_of_dates][0])

        order_of_dates+=1

    for a in range(350):
        for b in range(350):
            temp = []
            for dates in range(23):
                temp.append(correlation_datas[dates][a][b])
            standard_deviation[a][b]=np.std(temp)

    with open("standarddeviation.csv","a",encoding="utf8")as fw:
        for a in range(350):
            for b in range(350):
                fw.write(str(standard_deviation[a][b]))
                fw.write(",")
            fw.write("\n")

