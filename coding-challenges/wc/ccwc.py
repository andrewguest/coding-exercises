import argparse
import os


def count_bytes(filename: str) -> int:
    return os.path.getsize(filename)


def count_lines(filename: str) -> int:
    line_count = 0

    with open(filename, "r") as file:
        for _ in file:
            line_count += 1

    return line_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ccwc",
        description="Coding Challenges implementation of wc"
    )

    # CLI arguments
    parser.add_argument("-c", help="Returns the number of bytes in a file", action="store_true")
    parser.add_argument("-l", help="Returns the number of lines in a file", action="store_true")
    parser.add_argument("filename")  # last positional argument is the file to be processed

    args = parser.parse_args()

    if args.c:
        print(f"\t{count_bytes(args.filename)} {args.filename}")
    elif args.l:
        print(f"\t{count_lines(args.filename)} {args.filename}")