from fastapi.testclient import TestClient
from api import schedulerApp

client = TestClient(schedulerApp)

def test_getSchedule():
    response = client.get("/schedule/duration=17_break=5_start-date=2022-01-25_start-time=17:00_end-time=18:00")
    assert response.status_code == 200
    assert response.json() ==   {
                                    "data":[
                                            {"id":"20bce1800","date":"2022-01-25","startTime":"17:00:00","endTime":"17:17:00"},
                                            {"id":"20bce1802","date":"2022-01-25","startTime":"17:22:00","endTime":"17:39:00"},
                                            {"id":"20bce1803","date":"2022-01-25","startTime":"17:44:00","endTime":"18:01:00"},
                                            {"id":"20bce1804","date":"2022-01-26","startTime":"17:00:00","endTime":"17:17:00"},
                                            {"id":"20bce1805","date":"2022-01-26","startTime":"17:22:00","endTime":"17:39:00"}
                                            ],
                                    "length":5
                                 }   