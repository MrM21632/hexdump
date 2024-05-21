#!/usr/bin/env python3

import argparse


def read_license_file() -> str:
    """
    Read in the contents of the LICENSE file for the help message.
    """
    with open("LICENSE", "r", newline="") as license_file:
        contents = license_file.read()
    return contents

def read_file_as_bytes(filename: str) -> bytearray:
    """
    Read the contents of the file into a byte array.
    """
    binary_file = open(filename, 'rb')
    result = bytearray(binary_file.read())
    binary_file.close()

    return result


def read_file_contents(filename: str) -> None:
    """
    Read the contents of the file passed in and display in hexadecimal.
    """
    buffer = read_file_as_bytes(filename)
    offset = 0

    for i in range(0, len(buffer), 16):
        chunk = bytearray(buffer[i:i + 16])
        line = "{:08x}  {:23}  {:23}  |{:16}|".format(
            i,
            " ".join("{:02x}".format(x) for x in chunk[:8]),
            " ".join("{:02x}".format(x) for x in chunk[8:]),
            "".join(chr(x) if 32 <= x < 127 else "." for x in chunk),
        )

        offset += 16
        print(line)
    print("{:08x}".format(len(buffer)))


def hexdump():
    parser = argparse.ArgumentParser(
        prog='hexdump',
        description=(
            "Displays file contents in hexadecimal representation.\n"
            "Output matches canonical (-C) mode for the traditional hexdump(1) command."
        ),
        epilog=read_license_file(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        'filename',
        help='Name of the file to read in',
    )
    args = parser.parse_args()
    
    read_file_contents(args.filename)


if __name__ == "__main__":
    hexdump()