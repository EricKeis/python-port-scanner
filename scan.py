# main_script.py
import argparse
import port_scanner.scanner as scanner
import port_scanner.interface as interface

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a desired host address for open ports.")

    # Add a -g flag to determine which file to run
    parser.add_argument("-g", action="store_true", help="Run scanner in GUI mode. tkinter package required.")

    args = parser.parse_args()

    if args.g:
        interface.run()
    else:
        scanner.run()
