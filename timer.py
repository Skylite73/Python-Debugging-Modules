"""Timer module. Quick & Easy."""

import time
from functools import wraps


def timer(func):
    """Timer decorator."""
    @wraps(func)
    def timed(*args, **kwargs):
        print("---TIMER--- \tTIMER START")
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print("---TIMER--- \t%2.4f seconds to complete." % (finish-start))
        return result
    return timed
