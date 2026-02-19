from app.store.memory import campaigns,log
from app.agents.strategy_agent import strategy_agent
from app.agents.creative_agent import creative_agent

def generate_campaign(cid):

    campaign = campaigns[cid]

    log(cid,"Strategy agent running")

    strategy = strategy_agent(campaign["goal"])

    log(cid,"Creative agent running")

    creatives = creative_agent(campaign["goal"])

    campaign["strategy"]=strategy
    campaign["creatives"]=creatives
    campaign["status"]="AWAITING_SELECTION"

    log(cid,"Waiting for user selection")
