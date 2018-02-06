import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime

def plot_graph(name,x_value,y_value):
    fig = plt.figure()
    plt.title(name)
    ax1 = fig.add_subplot(111)
    ax1.plot(x_value, y_value)
    plt.xticks(rotation=30)
    plt.legend(loc=2, fontsize=10)
    plt.plot()
    plt.show()

def main():
    startdate=[]
    kospiindex=[]
    spxindex=[]
    ccmpindex=[]
    bbdxyindex=[]
    koacurncy=[]
    cl1comdty=[]
    bdiyindex=[]
    soxindex=[]
    xauindex=[]
    rbtacomdty=[]
    gvsk10yr=[]
    usggindex=[]
    gtdem10=[]
    fdfd=[]
    vkospu=[]
    visindex=[]
    with open("index4.csv", "r",encoding="utf8") as fr:
        lines=fr.readlines()
        for line in lines[1:]:
            contents=line.split(",")
            startdate.append(contents[0])
            kospiindex.append(float(contents[1]))
            spxindex.append(float(contents[2]))
            ccmpindex.append(float(contents[3]))
            bbdxyindex.append(float(contents[4]))
            koacurncy.append(float(contents[5]))
            cl1comdty.append(float(contents[6]))
            bdiyindex.append(float(contents[7]))
            soxindex.append(float(contents[8]))
            xauindex.append(float(contents[9]))
            rbtacomdty.append(float(contents[10]))
            gvsk10yr.append(float(contents[11]))
            usggindex.append(float(contents[12]))
            gtdem10.append(float(contents[13]))
            fdfd.append(float(contents[14]))
            vkospu.append(float(contents[15]))
            visindex.append(float(contents[16][:-1]))
    print("done")
    print(startdate)
    print(kospiindex)
    converted_dates=[]

    for date in startdate:
        converted_dates.append(datetime.datetime.strptime(date,"%Y-%m-%d"))

    # 행동이 3번 이상 반복이 된다면 함수로 만들어야한다
    plot_graph("kospi index",converted_dates,kospiindex)
    plot_graph("spxindex",converted_dates,spxindex)
    plot_graph("ccmpindex", converted_dates, ccmpindex)
    plot_graph("bbdxyindex", converted_dates, bbdxyindex)
    plot_graph("koacurncy", converted_dates, koacurncy)
    plot_graph("cl1comdty", converted_dates, cl1comdty)
    plot_graph("bdiyindex", converted_dates, bdiyindex)
    plot_graph("soxindex", converted_dates, soxindex)
    plot_graph("xauindex", converted_dates, xauindex)
    plot_graph("rbtacomdty", converted_dates, rbtacomdty)
    plot_graph("gvsk10yr", converted_dates, gvsk10yr)
    plot_graph("usggindex", converted_dates, usggindex)
    plot_graph("gtdem10", converted_dates, gtdem10)
    plot_graph("fdfd", converted_dates, fdfd)
    plot_graph("vkospu", converted_dates, vkospu)
    plot_graph("visindex", converted_dates, visindex)


#   항상 함수화를 시켜서 프로그램을 짜자
#   단순 명령어라도 def main()에 저장을 하고 if__name__으로 실행을 시키자
if __name__=="__main__":
    main()
