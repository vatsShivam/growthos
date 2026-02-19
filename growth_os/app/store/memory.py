campaigns = {}
activity = {}

def log(cid,msg):

    if cid not in activity:
        activity[cid] = []

    activity[cid].append(msg)
