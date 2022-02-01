"""
This is the main scheduler program
"""

# inport calendar - has a lot of functions related to dates, days, years, basically calendar
# import datetime;  now = datetime.datetime.now()
# above 2 imports required only if validation is supposed to be done, else not required

import copy

# function to schedule interviews after collecting basic info
def scheduler(dur, brk, curr_date, start_time, end_time):
    curr_time = copy.deepcopy(start_time)
    for rollno in candidates.keys():
        candidates[rollno]["date"] = ":".join([str(i) for i in curr_date])
        candidates[rollno]["start_time"] = ":".join([str(i) for i in curr_time])
        curr_time[1] += dur
        if (curr_time[1] >= 60):
            curr_time[1] -= 60
            curr_time[0] += 1            
        candidates[rollno]["end_time"] = ":".join([str(i) for i in curr_time])
        curr_time[1] += brk
        if (curr_time[1] >= 60):
            curr_time[1] -= 60
            curr_time[0] += 1 

        # checking if end_time is breached
        if (curr_time[0] >= end_time[0]):
            curr_time = copy.deepcopy(start_time)
            curr_date[0] += 1
            if (curr_date[0] > 31):
                curr_date[0] = 1
                curr_date[1] += 1  
                if (curr_date[1] > 12):
                    curr_date[1] = 1
                    curr_date[2] += 1
    
    '''
    # displaying scheduled timing
    for rollno in candidates.keys():
        print(candidates[rollno])
    '''
    
    # returning scheduled data
    return candidates

# raw data got from backend
candidates = {"20bce1800":{"name":"Raghu", "course":"CSE", "year":2020},
            "20bce1802":{"name":"Arvind", "course":"MECH", "year":2020},
            "20bce1803":{"name":"Vaishnavi", "course":"CSE", "year":2021},
            "20bce1804":{"name":"Gopal", "course":"ECE", "year":2022},
            "20bce1805":{"name":"Shivam", "course":"EEE", "year":2021}}

# sorting raw data based on year of candidate - ascending
candidates = dict(sorted(candidates.items(), key=lambda item: item[1]["year"]))
# wont be necessary as have to schedule in the order received (in case rescheduled to create void etc)
# better to include sorting in front end itself

'''
# function to collect basic info and call the scheduler from within this file
def call_scheduler():
    # collecting basic info of interview schedule
    dur = int(input("Enter duration of 1 interview (in minutes): "))
    brk = int(input("Enter duration of break after 1 interview (in minutes): "))
    start_date = list(map(int,input("Enter starting day of interviews (DD:MM:YYYY): ").split(":")))
    start_time = list(map(int,input("Enter starting time of interviews everyday (HH:MM) (24 Hr Format): ").split(":")))
    end_time = list(map(int,input("Enter ending time of interviews everyday (HH:MM) (24 Hr Format): ").split(":")))

    # calling scheduler
    scheduler(dur, brk, start_date, start_time, end_time)
call_scheduler()
'''

# function to collect basic info and call the scheduler from api.py
def call_scheduler(dur, brk, st_dt, st_tm, end_tm):
    # collecting basic info of interview schedule
    dur = int(dur)
    brk = int(brk)
    start_date = list(map(int,st_dt.split(":")))
    start_time = list(map(int,st_tm.split(":")))
    end_time = list(map(int,end_tm.split(":")))

    # calling scheduler
    return scheduler(dur, brk, start_date, start_time, end_time)



