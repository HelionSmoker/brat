# (Br)aille P(at)tern
A tool for converting braille symbols to and from binary numbers.

## Use Cases
- **Accessibility**: Braille is a tactile writing system used by people who are blind or visually impaired. This project could be used to create Braille symbols that can be printed out and used to label objects or identify locations in a space.

- **Art and Design**: Braille symbols can be used to create interesting and unique designs. This project could be used to create custom Braille patterns that can be incorporated into artwork or design projects.

- **⢹⠁⣟ ⡱⢎ ⢹⠁ converters**: The program could take in a string of text, convert it into Braille symbols, and output them as ASCII art or even as a physical embossed printout.

## Logic
There are 8 bits that represent the possible positions where a dot may be present in a Braille symbol: 4 bits for the first column, and 4 for the last. A value of 1 indicates the presence of a dot, while 0 indicates the absence. 

In total, there are 256 braille symbols (2^8), so their binary values range from `00000000` to `11111111`. This allows for fast conversion between the symbols and their binary value.

## Usage
To encode braille symbols, simply pass in the binary string patterns that represent the symbol:

``` sh
python brat.py 10001111 1 11111001 1111 111111 # ⢹⠁⣏⡇⡟
python brat.py --row 11010101 1 11101011 10101010 11111010 # ⢹⠁⣏⡇⡟
```

> Trailing zeros can be omitted.

To decode braille symbols to their corresponding binary pattern, pass in the symbols to `brat`.

```sh
python brat.py ⣒ ⡱ # 01010101 10010110
python brat.py --row ⣒ ⡱ # 01010101 10010110
```

## Installation
Simply clone the GitHub repository you should be good to go!

```sh
git clone https://github.com/your-username/brat.git
cd brat
python brat.py 1011101
```

## Future plans
- [ ] Add support for decoding symbols
- [ ] Add `--row` and `--col` flags
- [ ] Add support for ascii converters
- [ ] Add suport for text to embossed braille printout
- [ ] Use `argparse` instead of manual parsing

## Contributing
Contributions are highly appreciated! If you have any suggestions, please don't hesitate to open an issue or pull request.
