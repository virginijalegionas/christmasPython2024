def getCompleted(timeWorked, totalTime):
    
    # convert string to time
    workedHours, workedMinutes, workedSeconds = map(int, timeWorked.split(":"))
    totalHours, totalMinutes, totalSeconds = map(int, totalTime.split(":"))

    #calculate time in seconds
    secondsTimeWorked = workedHours * 3600 + workedMinutes * 60 + workedSeconds
    secondsTotalTime = totalHours * 3600 + totalMinutes * 60 + totalSeconds
    
    percentage = (secondsTimeWorked / secondsTotalTime) * 100
    return round(percentage)


print(getCompleted('01:00:00', '03:00:00')) # 33%
print(getCompleted('02:00:00', '04:00:00')) # 50%
print(getCompleted('01:00:00', '01:00:00')) # 100%
print(getCompleted('00:10:00', '01:00:00')) # 17%
print(getCompleted('01:10:10', '03:30:30')) # 33%
print(getCompleted('03:30:30', '05:50:50')) # 60%
print(getCompleted('28:00:00', '30:00:00')) # 93%
