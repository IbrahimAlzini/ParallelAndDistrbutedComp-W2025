#this is not necessary, is us organizing stuff

from src.tasks import power 

def dispatch():
    result_objs = [
        power.apply_async((number, 2)) for number in range (1, 10001)
    ]
    results = [
        result.get() for result in result_objs
    ]
    return results