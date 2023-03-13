import argparse
import data

parser = argparse.ArgumentParser(
    description="Encode or decode Braille symbols.")

parser.add_argument("pattern",
                    nargs="+",
                    metavar="PATTERN",
                    help="the binary representation of a Braille symbol")
parser.add_argument("-r",
                    "--by-row",
                    action="store_true",
                    help="treat PATTERN as the rows of a Braille symbol")
parser.add_argument("-a",
                    "--ascii",
                    action="store_true",
                    help="convert an ASCII character to a Braille symbol")
parser.add_argument("-e",
                    "--encode",
                    action="store_true",
                    help="convert a Braille symbol to binary")
parser.add_argument("-f",
                    "--format",
                    action="store_true",
                    help="make the output more readable")
parser.add_argument("-v",
                    "--version",
                    action="version",
                    version="%(prog)s 0.2.0")


def bin_to_braille(pattern: str, symbols: list[str]) -> str:
    """
    Given a dot pattern, convert it to an decimal index and return the symbol.
    """

    pattern = pattern.ljust(8, '0')
    return symbols[int(pattern, 2)]


def braille_to_bin(symbol: str, symbols: list[str]) -> str:
    """
    Given a braille symbol, return a binary repr of its index in `symbols`.
    """

    index = symbols.index(symbol)
    return bin(index)[2:].rjust(8, '0')


args = parser.parse_args()

if args.ascii:
    results = [data.ASCII[char] for char in args.pattern]
elif args.encode:
    results = [
        braille_to_bin(pattern, data.BY_ROW if args.by_row else data.BY_COL)
        for pattern in args.pattern
    ]
else:
    results = [
        bin_to_braille(pattern, data.BY_ROW if args.by_row else data.BY_COL)
        for pattern in args.pattern
    ]

if args.format:
    print('\n'.join([
        f"{args.pattern[i]} -> {result}" for i, result in enumerate(results)
    ]))
else:
    print(' '.join(results))

assert braille_to_bin("⢕", data.BY_COL) == "10100101"
assert braille_to_bin("⢕", data.BY_ROW) == "10011001"

assert bin_to_braille("", data.BY_COL) == "⠀"
assert bin_to_braille("01", data.BY_COL) == "⠂"
assert bin_to_braille("10100101", data.BY_COL) == "⢕"

assert bin_to_braille("", data.BY_ROW) == "⠀"
assert bin_to_braille("01", data.BY_ROW) == "⠈"
assert bin_to_braille("10011001", data.BY_ROW) == "⢕"
