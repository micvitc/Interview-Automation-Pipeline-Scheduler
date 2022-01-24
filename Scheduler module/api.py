from fastapi import FastAPI
import scheduler as sch

scheduler = FastAPI()

@scheduler.get("/schedule/duration={dur}_break={brk}_start-date={st_dt}_start-time={st_tm}_end-time={end_tm}")
async def get_schedule(dur, brk, st_dt, st_tm, end_tm):
    return sch.call_scheduler(dur, brk, st_dt, st_tm, end_tm)

# example - http://127.0.0.1:8000/schedule/duration=17_break=5_start-date=25:01:2022_start-time=17:00_end-time=18:00

