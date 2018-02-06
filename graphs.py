import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    fig=plt.figure()
    plt.title("kospi index")
    ax1=fig.add_subplot(111)
    ax1.plot(startdate,kospiindex)
    plt.plot()
    plt.show()

    fig = plt.figure()
    plt.title("spx index")
    ax1 = fig.add_subplot(111)
    ax1.plot(startdate, spxindex)
    plt.plot()
    plt.show()

if __name__=="__main__":
    main()
