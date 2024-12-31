from datetime import datetime


def getCompleted(timeWorked, totalTime):
    timeFormat = "%H:%M:%S"

    # convert string to time
    convertedTimeWorked = datetime.strptime(timeWorked, timeFormat)
    convertedTotalTime = datetime.strptime(totalTime, timeFormat)

    #get time in seconds
    secondsTimeWorked = convertedTimeWorked.hour * 3600 + convertedTimeWorked.minute * 60 + convertedTimeWorked.second
    secondsTotalTime = convertedTotalTime.hour * 3600 + convertedTotalTime.minute * 60 + convertedTotalTime.second
    
    percentage = (secondsTimeWorked / secondsTotalTime) * 100
    return round(percentage)




print(getCompleted('01:00:00', '03:00:00')) # 33%
print(getCompleted('02:00:00', '04:00:00')) # 50%
print(getCompleted('01:00:00', '01:00:00')) # 100%
print(getCompleted('00:10:00', '01:00:00')) # 17%
print(getCompleted('01:10:10', '03:30:30')) # 33%
print(getCompleted('03:30:30', '05:50:50')) # 60%





