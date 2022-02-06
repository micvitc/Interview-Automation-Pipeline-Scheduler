from datetime import date, time
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import scheduler as sch

app = FastAPI()

class Item(BaseModel):
    regNo: str
    name: str
    course: str
    year: int
    date: date
    startTime: time
    endTime: time

class Items(BaseModel):
    candidates: List[Item]

@app.get("/schedule/duration={duration}_break={brk}_start-date={startDate}_start-time={startTime}_end-time={endTime}", response_model=Items)
async def get_schedule(duration, brk, startDate, startTime, endTime):
    sch.callScheduler(duration, brk, startDate, startTime, endTime)
    scheduledData = []
    for key,val in sch.candidates.items():
        val["regNo"] = key
        scheduledData.append(val)
    return {"candidates": scheduledData}

# example - http://127.0.0.1:8000/schedule/duration=17_break=5_start-date=2022-01-25_start-time=17:00_end-time=18:00