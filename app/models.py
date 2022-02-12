from typing import List
from pydantic import BaseModel
from datetime import date, time


class Item(BaseModel):
    id: str
    date: date
    startTime: time
    endTime: time

class Items(BaseModel):
    data: List[Item]
    length: int