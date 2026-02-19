def growth_engine(metrics):

    if metrics["cpl"] > 180:
        return "Reduce budget"

    if metrics["ctr"] > 4:
        return "Increase budget"

    return "No action"
