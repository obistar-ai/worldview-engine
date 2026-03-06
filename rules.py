def evaluate(event):
    if event.name == "temperature" and event.value > 80:
        return True
    return False
