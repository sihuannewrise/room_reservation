from typing import Optional

from pydantic import BaseModel, Field

class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, max_length=100,)
    description: Optional[str]

    class Config:
        title = 'Базовый класс для переговорок'
        min_anystr_length = 1


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)

    class Config:
        title = 'Класс для создания переговорок'


class MeetingRoomUpdate(MeetingRoomBase):
    pass


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        title = 'Класс со схемой ответа из БД'
        orm_mode = True
