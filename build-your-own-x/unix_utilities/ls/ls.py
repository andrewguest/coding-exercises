import argparse
from pathlib import Path


class InvalidDirectoryInputError(Exception):
    def __dir__(self, message="Input is not a directory"):
        self.message = message

        super().__init__(self.message)


def read_directory(directory):
    if Path(directory).is_dir():
        for child in Path(directory).iterdir():
            print(child)
    else:
        raise InvalidDirectoryInputError


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Ls",
        description="Print the child files/folders of a given directory."
    )
    parser.add_argument("directory")

    args = parser.parse_args()

    read_directory(args.directory)
