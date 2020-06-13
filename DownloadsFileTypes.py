import os
from os import listdir
from os.path import isfile, join
import shutil

onlyfiles = [f for f in listdir("C:/Users/brian/Downloads") if isfile(join("C:/Users/brian/Downloads",f))]
extensioname = []

print(onlyfiles)




def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

  
# Parent Directory path 
parent_dir = "C:/Users/brian/My Documents/DownloadsFiles"

i = 0
while(i < len(onlyfiles)):
    x = 0
    ask = False
    tear = ""
    while(x < len(onlyfiles[i])):
        purse = 0
        happy = ""
        if(ask == True):
            tear += onlyfiles[i][x]
        if(onlyfiles[i][x] == "."):
            purse = len(onlyfiles[i])
            happy = onlyfiles[i][x + 1:purse]
            if("." not in happy):
                ask = True
        x += 1
    tear = tear.lower()
    if(tear not in extensioname and tear != ""):
        if(hasNumbers(tear) == False):
            extensioname.append(tear)
            # Path 
            directory = tear + "_files"
            path = os.path.join(parent_dir, directory) 
            os.mkdir(path) 
    shutil.copy("C:/Users/brian/Downloads/" + onlyfiles[i], "C:/Users/brian/Documents/DownloadsFiles/" + tear + "_files")
    i += 1

print("to")

onlyfiles1 = [f for f in listdir("C:/Users/brian/Documents/DownloadsFiles/") if isfile(join("C:/Users/brian/Documents/DownloadsFiles/",f))]
parent_dir1 = "C:/Users/brian/My Documents/DownloadsFiles/"
directory1 = "randomfiles"
path1 = os.path.join(parent_dir1, directory1) 
os.mkdir(path1) 
w = 0
while(w < len(onlyfiles1)):
    shutil.copy("C:/Users/brian/My Documents/DownloadsFiles/" + onlyfiles1[w], "C:/Users/brian/Documents/DownloadsFiles/randomfiles")
    os.remove(parent_dir1 + onlyfiles1[w])
    w += 1

