"""
This is the main scheduler program
"""

from datetime import datetime, timedelta, date, time

# function to schedule interviews after collecting basic info
def scheduler(duration, brk, currDate, startTime, endTime):
    currTime = startTime
    for rollNo in candidates.keys():
        candidates[rollNo]["date"] = currDate.date()
        candidates[rollNo]["startTime"] = currTime.time()
        currTime += timedelta(minutes = duration)
        candidates[rollNo]["endTime"] = currTime.time()
        currTime += timedelta(minutes = brk)

        # checking if endTime is breached
        if (currTime.hour >= endTime.hour):
            currTime = startTime
            currDate += timedelta(days = 1)
    
    '''
    # displaying scheduled timing
    for rollNo in candidates.keys():
        print(candidates[rollNo])
    '''
    
    # returning scheduled data
    return candidates

# raw data got from backend
candidates = {
            "20bce1800":{"name":"Raghu", "course":"CSE", "year":2020},
            "20bce1802":{"name":"Arvind", "course":"MECH", "year":2020},
            "20bce1803":{"name":"Vaishnavi", "course":"CSE", "year":2021},
            "20bce1804":{"name":"Gopal", "course":"ECE", "year":2022},
            "20bce1805":{"name":"Shivam", "course":"EEE", "year":2021}
            }

'''
# function to collect basic info and call the scheduler from within this file
def callScheduler():
    # collecting basic info of interview schedule
    duration = int(input("Enter durationation of 1 interview (in minutes): "))
    brk = int(input("Enter durationation of break after 1 interview (in minutes): "))
    startDate = datetime.fromisoformat(input("Enter starting day of interviews (YYYY-MM-DD): "))
    startTime = datetime.combine(date(1,1,1), time.fromisoformat(input("Enter starting time of interviews everyday (HH:MM) (24 Hr Format): ")))
    endTime = datetime.combine(date(1,1,1), time.fromisoformat(input("Enter ending time of interviews everyday (HH:MM) (24 Hr Format): ")))

    # calling scheduler
    scheduler(duration, brk, startDate, startTime, endTime)
callScheduler()
'''

# function to collect basic info from api.py and call the scheduler 
def callScheduler(duration, brk, startDate, startTime, endTime):
    # collecting basic info of interview schedule
    duration = int(duration)
    brk = int(brk)
    startDate = datetime.fromisoformat(startDate)
    startTime = datetime.combine(date(1,1,1), time.fromisoformat(startTime))
    endTime = datetime.combine(date(1,1,1), time.fromisoformat(endTime))

    # calling scheduler
    return scheduler(duration, brk, startDate, startTime, endTime)



