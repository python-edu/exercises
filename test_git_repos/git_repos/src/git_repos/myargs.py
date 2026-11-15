import argparse


def parse_arguments() -> argparse.Namespace:
    """Read the --full-paths option and return the parsed arguments."""
    parser = argparse.ArgumentParser(
                    prog='gitrepos',
                    description='Show repository placed in hom directory')

    parser.add_argument("-f", "--full-paths", action="store_true")
    return parser.parse_args()
