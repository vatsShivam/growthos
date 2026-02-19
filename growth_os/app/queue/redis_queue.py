import redis
from rq import Queue

redis_conn = redis.Redis()

campaign_queue = Queue(
    "campaigns",
    connection=redis_conn
)
