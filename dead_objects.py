from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, time

class DEAD_SONG(BaseModel):
    songId: int
    title: str
    firstPlayed: datetime
    firstPlayedShowId: str
    lastPlayed: datetime
    lastPlayedShowId: str
    countPlayed: int
    shortestSeconds: int
    shortestShowId: str
    longestSeconds: int
    longestShowId: str


class DEAD_SET_SONG(BaseModel):
    songSequence: int
    songId: str
    title: str
    segue: bool
    daysSincePlayed: int
    lengthSeconds: int

class DEAD_SET(BaseModel):
    setId: str
    sequence: int
    runningLegthSeconds: Optional[int] = None
    songs: List[DEAD_SET_SONG]

class DEAD_VENUE(BaseModel):
    venueId: str
    venue: str
    city: str
    state: str
    country: str

class DEAD_SHOW(BaseModel):
    showId: str
    showDate: datetime
    dayName: Optional[str] = None
    venueId: str
    venue: str
    city: str
    state: str
    country: str
    runningLengthSeconds: Optional[int] = None
    sets: List[DEAD_SET]


