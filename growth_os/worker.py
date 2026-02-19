
from rq import Worker
from app.queue.redis_queue import redis_conn

worker = Worker(["campaigns"],connection=redis_conn)
worker.work()
