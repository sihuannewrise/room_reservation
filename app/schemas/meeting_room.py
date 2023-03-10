from typing import Optional

from pydantic import BaseModel, Field, validator

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

    class Config:
        title = 'Класс для обновления переговорок'

    @validator('name')
    def name_cannot_be_null(cls, value: str):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        title = 'Класс со схемой ответа из БД'
        orm_mode = True
