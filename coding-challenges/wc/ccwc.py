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


def count_words(filename: str) -> int:
    word_count = 0

    with open(filename, "r") as file:
        content = file.read()
        word_count = len(content.split())

    return word_count


def count_characters(filename: str) -> int:
    character_count = 0

    with open(filename, "rb") as file:
        content = file.read()
        character_count = len(content)
        return character_count


def main():
    parser = argparse.ArgumentParser(
        prog="ccwc", description="Coding Challenges implementation of wc"
    )

    # CLI arguments
    parser.add_argument(
        "-c", help="Returns the number of bytes in a file", action="store_true"
    )
    parser.add_argument(
        "-l", help="Returns the number of lines in a file", action="store_true"
    )
    parser.add_argument(
        "-w", help="Returns the number of words in a file", action="store_true"
    )
    parser.add_argument(
        "-m", help="Returns the number of characters in a file", action="store_true"
    )
    parser.add_argument(
        "filename"
    )  # last positional argument is the file to be processed

    args = parser.parse_args()

    if args.c:
        print(f"\t{count_bytes(args.filename)} {args.filename}")
    elif args.l:
        print(f"\t{count_lines(args.filename)} {args.filename}")
    elif args.w:
        print(f"\t{count_words(args.filename)} {args.filename}")
    elif args.m:
        print(f"\t{count_characters(args.filename)} {args.filename}")
    else:
        print(
            f"\t{count_lines(args.filename)}\t{count_words(args.filename)}\t{count_characters(args.filename)} {args.filename}"
        )


if __name__ == "__main__":
    main()
