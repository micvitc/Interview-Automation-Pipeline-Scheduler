"""
This is the main scheduler program
"""

from datetime import datetime, timedelta, date, time

# function to schedule interviews after collecting basic info
def scheduler(duration, brk, currDate, currTime, endTime):
    for id in input["ids"]:
        candidate = dict()
        candidate["id"] = id
        candidate["date"] = currDate.date()
        candidate["startTime"] = currTime.time()
        currTime += timedelta(minutes = duration)
        candidate["endTime"] = currTime.time()
        currTime += timedelta(minutes = brk)
        output["data"].append(candidate)

        # checking if endTime is breached
        if (currTime.hour >= endTime.hour):
            currTime = input["startTime"]
            currDate += timedelta(days = 1)
    
    output["length"] = len(output["data"])

    # returning scheduled data
    return output

# raw data got from backend
input = {
            "ids":["20bce1800","20bce1802","20bce1803","20bce1804","20bce1805"],
            "duration": 0,
            "brk": 0, 
            "startDate": 0,
            "startTime": 0,
            "endTime": 0 
        }

output = {
            "data": [],
            "length": 0
         }

'''
# required code to call scheduler from within "scheduler.py" for debugging purposes

# raw data got from backend
input = {
            "ids":["20bce1800","20bce1802","20bce1803","20bce1804","20bce1805"],
            "duration": 15, # (in minutes)
            "brk": 5, # (in minutes)
            "startDate": datetime.fromisoformat('2022-02-06'), # (YYYY-MM-DD)
            "startTime": datetime.combine(date(1,1,1), time.fromisoformat("17:00")), # (HH:MM) (24 Hr Format)
            "endTime": datetime.combine(date(1,1,1), time.fromisoformat("18:00")) # (HH:MM) (24 Hr Format)
        }

# calling scheduler
scheduler(input["duration"], input["brk"], input["startDate"], input["startTime"], input["endTime"])
'''

# function to collect basic info from api.py and call the scheduler 
def callScheduler(duration, brk, startDate, startTime, endTime):
    # collecting basic info of interview schedule
    input["duration"] = int(duration)
    input["brk"] = int(brk)
    input["startDate"] = datetime.fromisoformat(startDate)
    input["startTime"] = datetime.combine(date(1,1,1), time.fromisoformat(startTime))
    input["endTime"] = datetime.combine(date(1,1,1), time.fromisoformat(endTime))

    # calling scheduler
    return scheduler(input["duration"], input["brk"], input["startDate"], input["startTime"], input["endTime"])

# datetime object is used even for just date and time bcoz 
# timedelta fn can be used only on datetime objects, 
# but while returning, datetime is converted to 
# date & time objects separately and returned
