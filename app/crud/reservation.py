from datetime import datetime

from sqlalchemy import and_, select
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
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.meetingroom_id == meetingroom_id,
                and_(
                    Reservation.from_reserve <= to_reserve,
                    Reservation.to_reserve >= from_reserve,
                ),
            )
        )
        reservations = reservations.scalars().all()
        return reservations


reservation_crud = CRUDReservation(Reservation)
