import random

def launch_agent(platforms,budget,creative):

    launches=[]

    for p in platforms:
        launches.append({
            "platform":p,
            "campaign_id":f"{p}_{random.randint(1000,9999)}",
            "status":"LIVE"
        })

    return launches
