from datetime import datetime

from pydantic import BaseModel, root_validator, validator

class ReservationBase(BaseModel):
    from_reserve: datetime
    to_reserve: datetime

    class Config:
        title = 'Базовый класс для бронирований'


class ReservationUpdate(ReservationBase):

    class Config:
        title = 'Класс для обновления бронирования'

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть позже времени окончания'
            )
        return values


class ReservationCreate(ReservationUpdate):
    meetingroom_id: int

    class Config:
        title = 'Класс для создания бронирования'


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int

    class Config:
        title = 'Класс бронирования со схемой ответа из БД'
        orm_mode = True
