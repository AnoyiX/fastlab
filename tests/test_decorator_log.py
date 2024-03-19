import asyncio
import time
from fastlab.decorators import LogExecTime, LogExecTimeAsync


@LogExecTime
def log_sleep():
    time.sleep(1.5)


@LogExecTimeAsync
async def log_sleep_async():
    await asyncio.sleep(1.5)


log_sleep()
asyncio.run(log_sleep_async())
