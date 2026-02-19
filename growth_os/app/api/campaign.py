from fastapi import APIRouter
from app.store.memory import campaigns,activity
from app.queue.redis_queue import campaign_queue
from app.workers.generate_worker import generate_campaign
from app.workers.launch_worker import launch_campaign
from app.workers.metrics_worker import run_metrics

router = APIRouter(prefix="/campaign")

counter = 1


@router.post("/create")
def create(data:dict):

    global counter
    cid = counter
    counter += 1

    campaigns[cid]={
        "id":cid,
        "goal":data["goal"],
        "budget":data["budget"],
        "status":"GENERATING"
    }

    campaign_queue.enqueue(generate_campaign,cid)

    return {"campaign_id":cid}
