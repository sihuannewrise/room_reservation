from datetime import datetime

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.reservation import reservation_crud
from app.api.validators import check_meeting_room_exists, check_reservation_intersections
from app.schemas.reservation import (
    ReservationCreate, ReservationUpdate, ReservationDB
)

router = APIRouter()

@router.post(
    '/',
    response_model=ReservationDB,
    response_model_exclude_none=True,
)
async def create_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(get_async_session),
) -> ReservationDB:
    await check_meeting_room_exists(reservation.meetingroom_id, session)
    await check_reservation_intersections(
        from_reserve=reservation.from_reserve,
        to_reserve=reservation.to_reserve,
        meetingroom_id=reservation.meetingroom_id,
        session=session,
    )
    new_reservation = await reservation_crud.create(reservation, session)
    return new_reservation