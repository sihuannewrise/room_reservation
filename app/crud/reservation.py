from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.reservation import Reservation


class CRUDReservation(CRUDBase):

    async def get_reservations_at_the_same_time(
        self,
        from_reserve: datetime,
        to_reserve: datetime,
        meetingroom_id: int,
        session: AsyncSession,
    ) -> list[Reservation]:
        db_reservations = await session.execute(
            select(Reservation).where(
                Reservation.meetingroom_id == meetingroom_id and
                Reservation.from_reserve < to_reserve and
                Reservation.to_reserve > from_reserve,
            )
        )
        db_reservations = db_reservations.scalars().all()
        return []


reservation_crud = CRUDReservation(Reservation)
