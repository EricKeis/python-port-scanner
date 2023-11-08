# main_script.py
import argparse
from importlib import util
import scanner
import interface

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a file based on command line flags.")

    # Add a -g flag to determine which file to run
    parser.add_argument("-g", action="store_true", help="Run file1 if specified, else run file2")

    args = parser.parse_args()

    if args.g:
        interface.run()
    else:
        scanner.run()
