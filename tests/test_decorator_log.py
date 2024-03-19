import time
from fastlab.decorators import LogExecTime


@LogExecTime
def log_sleep():
    time.sleep(1.5)


log_sleep()
