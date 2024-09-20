from functools import wraps
import time

def log_execution_time(func):
    # @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Funktion: {func.__name__} Dauer: {execution_time:.5f} sek")
        return result
    return wrapper



@log_execution_time
def slow_function():
    time.sleep(2)
    return "fertig"

slow_function()