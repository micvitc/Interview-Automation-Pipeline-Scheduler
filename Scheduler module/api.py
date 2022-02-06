from dataclasses import dataclass
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
import scheduler as sch

app = FastAPI()

class Item(BaseModel):
    regno: str
    name: str
    course: str
    year: int
    date: str
    start_time: str
    end_time: str

class Items(BaseModel):
    candidates: List[Item]

@app.get("/schedule/duration={dur}_break={brk}_start-date={st_dt}_start-time={st_tm}_end-time={end_tm}", response_model=Items)
async def get_schedule(dur, brk, st_dt, st_tm, end_tm):
    sch.call_scheduler(dur, brk, st_dt, st_tm, end_tm)
    data = []
    for key,val in sch.candidates.items():
        val["regno"] = key
        data.append(val)
    return {"candidates": data}

# example - http://127.0.0.1:8000/schedule/duration=17_break=5_start-date=25:01:2022_start-time=17:00_end-time=18:00