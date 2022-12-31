from typing import Optional
from pydantic import BaseModel, Field, validator


class MeetingRoomCreate(BaseModel):
    name: str = Field(
        ..., max_length=100,
        title='Название', description='Описание',
    )
    description: Optional[str]

    class Config:
        title = 'Класс для создания переговорок'
        min_anystr_length = 2

    @validator('name')
    def name_cant_be_numeric(cls, value: str):
        if value.isnumeric():
            raise ValueError('Имя не может быть числом')
        return value
