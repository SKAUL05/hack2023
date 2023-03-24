import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args):
        start_time = time.time()
        retval = func(*args)
        print("Function Executed in : ", time.time() - start_time, "secs")
        return retval

    return wrapper


