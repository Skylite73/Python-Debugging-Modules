# Debugger module by Ky Eltis.

class DebugStream():
    """Houses debug data for one stream/table."""

    def __init__(self, header, row1) -> None:
        """Init."""
        self.header: list[str] = header
        self.rows: list[list[str]] = [row1]
        self.lens: list[list[int]] = [[len(title) for title in header],
                                      [len(item) for item in row1]]

    def add_row(self, row: list[str]) -> None:
        """Gathers debug data to be passed onto debug_table."""
        self.rows.append(row)
        self.lens.append([len(var) for var in row])

    def merge_data(self, var_names, row) -> None:
        """Merge incompatible debug calls on the same stream."""
        pass


class Debugger():
    """Debug Class."""

    def __init__(self):
        """Init."""
        self.streams: dict[str, DebugStream] = {}

    def debug(self, locals: dict, var_string: str,
              stream: str = 'Stream 1') -> None:
        """Gathers debug data to be passed onto debug_table.

        Example use: debug(locals(), "[var1,var2]")
        """
        vars = {var.strip(): locals[var.strip()]
                for var in var_string.strip('][').split(',')}
        var_names = [var for var in vars]
        try:
            mystream = self.streams[stream]
            if all([var in mystream.header for var in var_names]):
                # All variables already accounted for in header
                mystream.add_row([str(locals[var]) for var in vars])
            else:
                # Merge data streams
                mystream.merge_data(var_names, vars)
        except KeyError:
            # New data stream
            row1 = [str(locals[var]) for var in vars]
            self.streams[stream] = DebugStream(var_names, row1)

    def table(self, stream: str = 'Stream 1', max_size: int = 12,
              min_size: int = 6, quiet: bool = False) -> list:
        """Tabulates debug data."""
        # lens = [max(len(str(locals[var])), debug.lens[i], 6)
        #             for i, var in enumerate(vars)]
        try:
            mystream = self.streams[stream]
            header = mystream.header
            rows = mystream.rows
            lens = [max(i) for i in zip(*mystream.lens)]
            col_sizes = [max(min_size, min(i, max_size)) for i in lens]
            data = []
            for i, size in enumerate(col_sizes):
                print(size)
                example = rows[0][i]
                try:
                    _ = float(example)
                    data.append("{:>%i}" % (size))
                except ValueError:
                    data.append("{:<%i}" % (size))
            formatting = '\t'.join(data)
            sep = ["-"*i for i in col_sizes]
            table = [formatting.format(*i) for i in [header, sep, *rows]]
            if not quiet:
                print(f"---DEBUGGER--- \tTABLE {stream} BEGIN")
                [print(i) for i in table]
                print(f"---DEBUGGER--- \tTABLE {stream} END")
            return table
        except KeyError:
            print(f"---DEBUGGER--- ERROR! \tNo debug set for '{stream}'")
            if stream == "Stream 1":
                print("Did you set the table stream for d.table()?")
            return []
