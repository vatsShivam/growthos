from app.store.memory import campaigns,log
from app.agents.platform_agent import platform_agent
from app.agents.launch_agent import launch_agent

def launch_campaign(cid):

    campaign = campaigns[cid]

    platforms = platform_agent(campaign["goal"])

    launch = launch_agent(
        platforms,
        campaign["budget"],
        campaign["selected"]
    )

    campaign["launch"]=launch
    campaign["status"]="LIVE"

    log(cid,"Campaign launched LIVE")
