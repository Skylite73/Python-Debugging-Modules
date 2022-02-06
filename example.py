# Example use of modules

try:
    """Works if Python-Debugging-Modules/ is in MYPYPATH or PYTHONPATH"""
    from timer import timer
except ModuleNotFoundError:
    """Temporarily adds modules to Python PATH"""
    import os
    import sys
    script_path = os.path.abspath(os.path.dirname(__file__))
    module_path = os.path.join(script_path, "Modules")  # Change to module path
    sys.path.append(module_path)
    from timer import timer     # type: ignore
from debugger import Debugger   # type: ignore
# from plotter import plotter   # type: ignore


@timer
def main():
    """Things are done here."""
    d = Debugger()
    for i in range(10):
        a = 10 ** i
        b = 'b'*i
        d.debug(locals(), "a,b", "table1")
    for i in range(10):
        a = 10 ** i
        b = 'b'*i
        c = i/9
        e = 1/a
        d.debug(locals(), "e,c,b,a", "table2")
    for i in range(10):
        c = i/9
        e = 1/(10 ** i)
        d.debug(locals(), "c,e", "table1")
    d.table("table1")
    d.table("table2")


if __name__ == '__main__':
    main()
