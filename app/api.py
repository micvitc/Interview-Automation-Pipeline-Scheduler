from datetime import date, time
from dotenv import dotenv_values
from fastapi import FastAPI

from app.modules.scheduler import scheduler as sch
from app.models import Items
from app.modules.collector.collect import Colletor

values = dotenv_values(".env")
schedulerApp = FastAPI()


@schedulerApp.get("/")
async def test() :
    return "Scheduler API is working"


@schedulerApp.get("/schedule/duration={duration}_break={brk}_start-date={startDate}_start-time={startTime}_end-time={endTime}", response_model=Items)
async def getSchedule(duration: int, brk: int, startDate: date, startTime: time, endTime: time):
    return sch.callScheduler(duration, brk, startDate, startTime, endTime)


@schedulerApp.get("/testCollector")
async def testCollector():
    c = Colletor(values['url'], values['list'], values['email'], values['pass'])
    res = c.collect()
    return res

# example - http://127.0.0.1:8000/schedule/duration=17_break=5_start-date=2022-01-25_start-time=17:00_end-time=18:00