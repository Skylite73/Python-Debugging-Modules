import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
from functools import wraps


def plotter(plot: bool = True):
    # Only False if you don't want a plot but have already coded it in
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mplstyle.use(['ggplot', 'fast'])
            fig, ax = plt.subplots()
            if plot:
                ax.set_aspect('equal', 'box')
                res = func(*args, ax=ax, **kwargs)
                fig.legend(loc='right')
                print("Plotting...")
                plt.show()
                return res
            else:
                return func(*args, ax, **kwargs)
        return wrapper
    return decorator
