def platform_agent(goal):

    if "b2b" in goal.lower():
        return ["linkedin"]

    return ["meta"]
