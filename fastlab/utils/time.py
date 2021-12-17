import time

class TimeUtils:

    @staticmethod
    def timestamp() -> int:
        """
        now timestamp(ms)
        """
        return int(time.time() * 1000)
