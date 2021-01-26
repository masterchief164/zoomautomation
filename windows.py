import webbrowser
import subprocess
import schedule
import time
import os


k = False
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path+"\windo.bat"


# tt
# 9-10 phy, 11-12 math
# 9 - 10 math, 11-12 phy
# 9-10 eng, 10-11 phy ,11-12 math ,2-5 IT lab
# 9-10 math 11-12 phy
# 9-10 eng 10-11 IT
# wed this week


def phy():
    global k
    webbrowser.open('https://zoom.us/j/95928624855?pwd=MmJtRER4MlduVlpJU0RXeVNmN0hVZz09')
    time.sleep(3600)
    k = True


def mat():
    global k
    webbrowser.open('https://zoom.us/j/3136940467?pwd=QTRaclVLeFpWZW1vSHpoNEwxU1F4UT09')
    time.sleep(3600)
    k = True


def eng():
    global k
    webbrowser.open("https://zoom.us/j/3537783014?pwd=blplRGkrZSs2RjAyS2RlYmMxQ0RGdz09")
    time.sleep(3600)
    k = True


def IT():
    global k
    webbrowser.open("https://zoom.us/j/92311038253?pwd=SFgrdHEzZC8rTERBK0pjSFdhZ3JNdz09")
    time.sleep(3600)
    k = True


schedule.every().monday.at("09:10").do(phy)
print("added phy monday")
schedule.every().monday.at("11:10").do(mat)
print("added math monday")
schedule.every().tuesday.at("09:10").do(mat)
print("added math tuesday")
schedule.every().tuesday.at("11:10").do(phy)
print("added phy tuesday")
schedule.every().wednesday.at("09:10").do(eng)
print("added eng wednesday")
schedule.every().wednesday.at("10:10").do(phy)
print("added phy wednesday")
schedule.every().wednesday.at("11:10").do(mat)
print("added math wednesday")
schedule.every().wednesday.at("14:10").do(IT)
print("added IT wednesday")
schedule.every().thursday.at("09:10").do(mat)
print("added math thursday")
schedule.every().thursday.at("11:10").do(phy)
print("added phy thursday")
schedule.every().friday.at("09:10").do(eng)
print("added eng friday")
schedule.every().friday.at("10:10").do(IT)
print("added IT friday")

while not k:
    k = False
    schedule.run_pending()
    time.sleep(1)
    

subprocess.call(dir_path)
