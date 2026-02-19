from app.store.memory import campaigns,log
from app.agents.metrics_agent import metrics_agent
from app.agents.growth_engine import growth_engine

def run_metrics(cid):

    metrics = metrics_agent()

    suggestion = growth_engine(metrics)

    campaigns[cid]["metrics"]=metrics
    campaigns[cid]["suggestion"]=suggestion

    log(cid,f"AI Suggestion: {suggestion}")
