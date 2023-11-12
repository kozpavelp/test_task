from redis import Redis


async def get_redis_connection():
    redis_client = Redis(host="redis", port=6379, db=0)
    try:
        yield redis_client
    finally:
        pass
