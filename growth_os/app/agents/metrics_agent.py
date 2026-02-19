import random

def metrics_agent():

    return {
        "ctr": round(random.uniform(1,5),2),
        "cpl": random.randint(80,250)
    }
