import argparse  # pragma: no cover

from . import base_function
from . import BaseClass


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m test_python_project` and `$ test_python_project `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(
        description="test_python_project.",
        epilog="Enjoy the test_python_project functionality!",
    )
    # This is required positional argument
    parser.add_argument(
        "name",
        type=str,
        help="The username",
        default="blink1073",
    )
    # This is optional named argument
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        help="The Message",
        default="Hello",
        required=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Optionally adds verbosity",
    )
    args = parser.parse_args()
    print(f"{args.message} {args.name}!")
    if args.verbose:
        print("Verbose mode is on.")

    print("Executing main function")
    base = BaseClass()
    print(base.base_method())
    print(base_function())
    print("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
