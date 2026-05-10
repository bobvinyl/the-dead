from pydantic import BaseModel
from datetime import datetime, time

def DEAD_SET_SONG(BaseModel):
    songSequence: int
    songId: str
    title: str
    segue: bool
    daysSincePlayed: int
    lengthSeconds: int

def DEAD_SET(BaseModel):
    setId: str
    sequence: int
    runningLegthSeconds: int
    songs: list[DEAD_SET_SONG]

def DEAD_SHOW(BaseModel):
    showId: str
    showDate: datetime
    dayName: str
    venueId: str
    venue: str
    city: str
    state: str
    country: str
    runningLengthSeconds: int
    sets: list[DEAD_SET]


