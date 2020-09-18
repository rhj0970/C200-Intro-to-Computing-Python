from os import listdir
from os.path import isfile, join, isdir

def show_directories(wdList):
#TO DO: Implement this function
    while wdList:
        x = wdList[0]
        wdList.remove(x)
        print(x)

        xList = [join(x,f) for f in listdir(x) if isdir(join(x,f))]
        if xList:
            wdList = xList + wdList


wd = input("working directory: ")
wdList = [join(wd,f) for f in listdir(wd) if isdir(join(wd,f))]

show_directories(wdList)
