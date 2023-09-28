import csv
import argparse
from itertools import islice
import random


def process_csv(input_file: str, output_file: str, shuffle: bool) -> None:
    with open(input_file, mode="r") as csv_file, open(
        output_file, mode="w"
    ) as txt_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            # Convert the row to a list of letter-value pairs, starting with 'a'
            letter_value_pairs = [
                f"{chr(ord('a') + i)}{val}" for i, val in enumerate(row)
            ]

            if shuffle:
                random.shuffle(letter_value_pairs)

            # Join the letter-value pairs with no spaces and write to the output file
            txt_file.write("".join(letter_value_pairs) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process a time-series CSV and convert it to a custom text format."
    )
    parser.add_argument("input_file", type=str, help="Path to the input CSV file.")
    parser.add_argument("output_file", type=str, help="Path to the output text file.")
    parser.add_argument(
        "--shuffle",
        action="store_true",
        help="Whether to shuffle the order of letter and value pairs.",
    )

    args = parser.parse_args()
    process_csv(args.input_file, args.output_file, args.shuffle)
