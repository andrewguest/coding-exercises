import argparse
import os


def parse_args(arg_list: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--bytes", action="store_true", help="Print the byte counts")
    parser.add_argument("-l", "--lines", action="store_true", help="Print the newline counts")
    parser.add_argument("-w", "--words", action="store_true", help="Print the word counts")
    parser.add_argument("-m", "--chars", action="store_true", help="Print the character counts")
    parser.add_argument("filename", help="File to count")

    # Parse the command line arguments
    return parser.parse_args(arg_list)


class PythonWC:
    def __init__(self, arg_list: list[str] | None = None) -> None:
        self.args: argparse.Namespace = parse_args(arg_list)

    def count_bytes(self) -> int:
        return os.stat(self.args.filename).st_size

    def count_lines(self) -> int:
        with open(self.args.filename, "r") as f:
            lines = len(f.readlines())
            
        return lines

    def count_words(self) -> int:
        word_count = 0

        with open(self.args.filename, "r") as f:
            data = f.read()
            lines = data.split()
            word_count += len(lines)

        return word_count

    def count_characters(self) -> int:
        # Start with the line count, because this counts all of the newline characters
        character_count = self.count_lines()

        with open(self.args.filename, "r") as f:
            data = f.read()
            character_count += len(data)
                
        return character_count

    def default_options(self) -> str:
        return f"{self.count_lines()} {self.count_words()} {self.count_bytes()} {self.args.filename}"


def main(arg_list: list[str] | None = None) -> None:
    wc_py = PythonWC(arg_list)

    if wc_py.args.bytes:
        result = f"{wc_py.count_bytes()} {wc_py.args.filename}" 
    elif wc_py.args.lines:
        result = f"{wc_py.count_lines()} {wc_py.args.filename}"
    elif wc_py.args.words:
        result = f"{wc_py.count_words()} {wc_py.args.filename}"
    elif wc_py.args.chars:
        result = f"{wc_py.count_characters()} {wc_py.args.filename}"
    else:
        result = wc_py.default_options()

    print(result)

if  __name__ == "__main__":
    main()
    