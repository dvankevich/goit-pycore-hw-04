import sys
from colorama import Fore, Style
from pathlib import PurePath, Path

FILE_COLOR = Fore.GREEN
DIR_COLOR = Fore.LIGHTBLUE_EX

def color_print(str, color):
    print(color + str + Style.RESET_ALL)

def help():
    print("help message for script "+  PurePath(sys.argv[0]).name)



def main():
    print(len(sys.argv))
    if len(sys.argv) == 1:
        help()
        sys.exit(22) # Invalid argument 
    elif len(sys.argv) > 2:
        help()
        sys.exit(7) # Argument list too long

    arg = sys.argv[1]
    if arg == "?" or arg == "/?" or arg == "-h" or arg == "--help":
        help()
        sys.exit()

    p = Path(arg)
    print(p)
    if not p.exists():
        print("path is not exist")
        sys.exit(2) # No such file or directory
    elif not p.is_dir():
        print("argument must be a directory")
        sys.exit(20) # Not a directory


if __name__ == "__main__":
    main()