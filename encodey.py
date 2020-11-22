#!/usr/bin/env python3

import sys

# Set color output
class color:
    YELLOW = '\033[1;33;48m'
    CYAN = '\033[1;36;48m'
    GREEN = '\033[1;32;48m'
    RED = '\033[1;31;48m'
    NC = '\033[1;37;0m'

# If user chooses single encode
def single_encode(payload):
    single_encoded_characters = {
            ":":"%3A",
            ";":"%3B",
            "<":"%3C",
            "=":"%3D",
            ">":"%3E",
            "@":"%40",
            "[":"%5B",
            "\\":"%5C",
            "]":"%5D",
            "^":"%5E",
            "{":"%7B",
            "|":"%7C",
            "}":"%7D",
            "/":"%2F",
            ".":"%2E",
            " ":"%20",
            "!":"%21",
            "\"":"%22",
            "#":"%23",
            "$":"%24",
            "%":"%25",
            "&":"%26",
            "'":"%27",
            "(":"%28",
            ")":"%29",
            "*":"%2A",
            "+":"%2B",
            ",":"%2C",
            "-":"%2D",
            "_":"%5F",
            "`":"%60",
    }

    # create empty list to hold split payload
    new_payload = []

    for char in payload:
        new_payload.append(char)

    # For each character in the payload, if the character is equal to the key, replace the character with the encoded value
    for char in new_payload:
        for key, value in single_encoded_characters.items():
            if char == key:
                new_payload = [c.replace(char, value) for c in new_payload]

    print(f"\n{color.CYAN}[ Original Payload ]:{color.NC} {color.RED}{payload}{color.NC}")
    print(f"{color.CYAN}[ Single Encoded Payload ]:{color.NC} {color.GREEN}{''.join(new_payload)}{color.NC}")

# If user choose double encoded payloads
def double_encode(payload):

    double_encoded_characters = {
            ":":"%253A",
            ";":"%253B",
            "<":"%253C",
            "=":"%253D",
            ">":"%253E",
            "@":"%2540",
            "[":"%255B",
            "\\":"%255C",
            "]":"%255D",
            "^":"%255E",
            "{":"%257B",
            "|":"%257C",
            "}":"%257D",
            "/":"%252F",
            ".":"%252E",
            " ":"%2520",
            "!":"%2521",
            "\"":"%2522",
            "#":"%2523",
            "$":"%2524",
            "%":"%2525",
            "&":"%2526",
            "'":"%2527",
            "(":"%2528",
            ")":"%2529",
            "*":"%252A",
            "+":"%252B",
            ",":"%252C",
            "-":"%252D",
            "_":"%255F",
            "`":"%2560",
    }

    # create empty list to hold split payload
    new_payload = []

    for char in payload:
        new_payload.append(char)

    # For each character in the payload, if the character is equal to the key, replace the character with the encoded value
    for char in new_payload:
        for key, value in double_encoded_characters.items():
            if char == key:
                new_payload = [c.replace(char, value) for c in new_payload]

    print(f"\n{color.CYAN}[ Original Payload ]:{color.NC} {color.RED}{payload}{color.NC}")
    print(f"{color.CYAN}[ Double Encoded Payload ]:{color.NC} {color.GREEN}{''.join(new_payload)}{color.NC}")


def main():
    # read line from system input
    for line in sys.stdin.readlines():
        line = str(line).strip("\n")
        # If user tries too many arguments...
        if len(sys.argv) > 2:
            print("Too many arguments given!")
            sys.exit(1)
        # Choose single encode if user does not specify
        elif len(sys.argv) < 2:
            single_encode(line)
        # Double encode
        elif sys.argv[1].lower() == "--double-encode":
            double_encode(line)
        # Single encode
        elif sys.argv[1].lower() == "--single-encode":
            single_encode(line)
        # If all else fails, do single encode
        else:
            single_encode(line)

if __name__ == "__main__":
    main()

