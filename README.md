# (Br)aille P(at)tern
A tool for converting braille symbols to and from binary numbers.

## Use Cases
- **Accessibility**: create Braille symbols that can be printed out and used to label objects or identify locations in a space.

- **Art and Design**: create custom Braille patterns that can be incorporated into artwork or design projects.

- **⢹⠁⣟ ⡱⢎ ⢹⠁ converters**: make physical embossed printout using Braille symbols

## Usage
To encode braille symbols, simply pass in the binary string patterns that represent the symbol:

``` sh
python brat.py 10001111 1 
# ⢹ ⠁
python brat.py --by-row 101011 101
# ⠧ ⠃
python brat.py --by-row --format 1011 111011
# 1011 -> ⠓
# 111011 -> ⠯
python brat.py -a A B C
# ⡁ ⡃ ⡉
```

> Trailing zeros can be omitted.

To decode braille symbols to their corresponding binary pattern, pass in the symbols to `brat`.

```sh
python brat.py -e ⣒ ⡱ 
# 01010101 10010110
python brat.py --by-row --encode ⣒ ⡱ 
# 00110011 10010110
```

## Installation
Simply clone the GitHub repository you should be good to go!

```sh
git clone https://github.com/your-username/brat.git
cd brat
python brat.py 1011101
```

## Logic
There are 8 bits that represent the possible positions where a dot may be present in a Braille symbol: 4 bits for the first column, and 4 for the last. A value of 1 indicates the presence of a dot, while 0 indicates the absence. 

In total, there are 256 braille symbols (2^8), so their binary values range from `00000000` to `11111111`. This allows for fast conversion between the symbols and their binary value.

## Future plans
- [x] Add support for decoding symbols
- [x] Add support for ascii converters
- [x] Use `argparse` instead of manual parsing
- [ ] Add suport for text to embossed braille printout
- [ ] Add pip support

## Contributing
Contributions are highly appreciated! If you have any suggestions, please don't hesitate to open an issue or pull request.
