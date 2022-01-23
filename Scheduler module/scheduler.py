"""
This is the main scheduler program
"""

# inport calendar - has a lot of functions related to dates, days, years, basically calendar
import datetime
import copy

# function to schedule interviews after collecting basic info
def schedule():
    int_date = copy.deepcopy(start_date)
    int_time = copy.deepcopy(start_time)
    for rollno in candidates.keys():
        candidates[rollno]["date"] = ":".join([str(i) for i in int_date])
        candidates[rollno]["start_time"] = ":".join([str(i) for i in int_time])
        int_time[1] += dur
        if (int_time[1] >= 60):
            int_time[1] -= 60
            int_time[0] += 1            
        candidates[rollno]["end_time"] = ":".join([str(i) for i in int_time])
        int_time[1] += brk
        if (int_time[1] >= 60):
            int_time[1] -= 60
            int_time[0] += 1 

        # checking if end_time is breached
        if (int_time[0] >= end_time[0]):
            int_time = copy.deepcopy(start_time)
            int_date[0] += 1
            if (int_date[0] > 31):
                int_date[0] = 1
                int_date[1] += 1  
                if (int_date[1] > 12):
                    int_date[1] = 1
                    int_date[2] += 1

    # displaying scheduled timing
    for rollno in candidates.keys():
        print(candidates[rollno])

# raw data got from backend
candidates = {"20bce1800":{"name":"Raghu", "course":"CSE", "year":2020},
            "20bce1802":{"name":"Arvind", "course":"MECH", "year":2020},
            "20bce1803":{"name":"Vaishnavi", "course":"CSE", "year":2021},
            "20bce1804":{"name":"Gopal", "course":"ECE", "year":2022},
            "20bce1805":{"name":"Shivam", "course":"EEE", "year":2021}}

# sorting raw data based on year of candidate - ascending
candidates = dict(sorted(candidates.items(), key=lambda item: item[1]["year"]))

# collecting basic info of interview schedule
dur = int(input("Enter duration of 1 interview (in minutes): "))
brk = int(input("Enter duration of break after 1 interview (in minutes): "))
start_date = list(map(int,input("Enter starting day of interviews (DD:MM:YYYY): ").split(":")))
start_time = list(map(int,input("Enter starting time of interviews everyday (HH:MM) (24 Hr Format): ").split(":")))
end_time = list(map(int,input("Enter ending time of interviews everyday (HH:MM) (24 Hr Format): ").split(":")))
now = datetime.datetime.now()

schedule()



