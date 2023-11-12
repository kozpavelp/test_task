from fastapi import APIRouter, HTTPException, Depends
from redis import Redis

from src.schemas.schemas import UserData
from src.db.redis_session import get_redis_connection

data_router = APIRouter()


@data_router.post('/write_data')
async def write_data(data: UserData, redis: Redis = Depends(get_redis_connection)):
    success = redis.set(data.phone, data.address)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to write data to database")
    return {'message': 'Success'}


@data_router.get('/check_data')
async def check_data(phone: str, redis: Redis = Depends(get_redis_connection)):
    address = redis.get(phone)
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return {'phone': phone, 'address': address}
