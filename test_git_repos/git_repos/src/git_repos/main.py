"""
...
"""

# local imports
from . import myargs


def main():
    args = myargs.parse_arguments()
    print(args)


if __name__ == "__main__":
    main()
