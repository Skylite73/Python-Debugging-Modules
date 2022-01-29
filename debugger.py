# Couldn't really be bothered to do global variables or funky things with
# classes so this might not work in some weirdly scoped systems.

def debug(locals: dict, var_string: str, num: int = 0) -> None:
    """Gathers debug data to be passed onto debug_table.

    Seperate data streams should be designated different nums.
    Example use: debug(locals(), "[var1,var2]")
    """
    vars = {var.strip(): locals[var.strip()]
            for var in var_string.strip('][').split(',')}
    try:
        debug.rows[num].append([str(locals[var] if isinstance(
            locals[var], list) else locals[var]) for var in vars])

        debug.lens[num] = [max(len(str(locals[var])), debug.lens[num][i], 6)
                           for i, var in enumerate(vars)]
    except AttributeError:
        # Runs on first debug call
        debug.rows = []
        debug.header = []
        debug.lens = []
        debug(locals, var_string, num)
    except IndexError:
        # Runs on first debug call for each num
        debug.rows.append([])
        debug.header.append([var for var in vars])
        debug.lens.append([len(var) for var in vars])
        debug(locals, var_string, num)


def debug_table(num: int = 0, max_col_size: int = 10, min_col_size: int = 6) -> list:
    """Tabulates debug data."""
    try:
        col_sizes = [min(max(i, 6), 10) for i in debug.lens[num]]
        data = []
        for i, size in enumerate(col_sizes):
            example = debug.rows[0][0][i]
            try:
                _ = float(example)
            except ValueError:
                data.append("{:>i}" % (size))
        data.append("{:>%i}" % (size))
        formatting = '\t'.join(data)
        sep = ["-"*i for i in col_sizes]
        table = [formatting.format(*i)
                 for i in [debug.header[num], sep, *debug.rows[num]]]
        print(f"---DEBUGGER--- \tTABLE {num} BEGIN")
        [print(i) for i in table]
        print(f"---DEBUGGER--- \tTABLE {num} END")
        return table

    except AttributeError:
        print(f"No debug set for num {num}")
        return False
