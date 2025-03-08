import argparse
from pathlib import Path


class InvalidFileInputError(Exception):
    def __init__(self, message="Input is not a file") -> None:
        self.message = message

        super().__init__(self.message)


def read_file(filename):
    if Path(filename).is_file():
        with open(filename, "r") as file:
            for line in file:
                print(line.rstrip())
    else:
        raise InvalidFileInputError


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Cat", description="Reads the contents of a given file, line-by-line."
    )
    parser.add_argument("filename")  # positional argument

    args = parser.parse_args()

    read_file(args.filename)
