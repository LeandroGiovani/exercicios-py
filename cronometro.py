import time

timerS = 0
newTimerS = ""
timerM = 0
newTimerM = ""
timerH = 0
newTimerH = ""

def formatTime():
    if timerS < 10:
        newTimerS = "0" + f"{timerS}"
    else:
        newTimerS = timerS

    if timerM < 10:
        newTimerM = "0" + f"{timerM}"
    else:
        newTimerM = timerM

    if timerH < 10:
        newTimerH = "0" + f"{timerH}"
    else:
        newTimerH = timerH

    return f"{newTimerH}:{newTimerM}:{newTimerS}"

while True:
    time.sleep(1)
    timerS += 1
    if timerS == 60:
        timerM += 1
        timerS = 0
    if timerM == 60:
        timerH += 1
        timerM = 0
    if timerH == 24:
        print("00:00:00")
        break
    print(formatTime())