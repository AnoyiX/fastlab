import time
from functools import wraps
from ..logging import logs


def LogExecTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            total_time = time.perf_counter() - start_time
            logs.info(f'Function `{func.__name__}` took {total_time:.4f} seconds')
    return wrapper


def LogExecTimeAsync(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            total_time = time.perf_counter() - start_time
            logs.info(f'Function `{func.__name__}` took {total_time:.4f} seconds')
    return wrapper
