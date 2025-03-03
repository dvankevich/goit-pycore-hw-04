import sys
import os
from colorama import Fore, Style
from pathlib import PurePath, Path

FILE_COLOR = Fore.GREEN
DIR_COLOR = Fore.LIGHTBLUE_EX
LINK_COLOR = Fore.LIGHTMAGENTA_EX
MARGIN = "  "
depth = 0 # directory depth value

def color_print(str, color):
    '''
    Print string str with color
    Args:
        str (str): string to print
        color: color constant from colorama library
    '''
    print(color + str + Style.RESET_ALL)

def help():
    '''
    Show help and usage message.
    '''
    print("Lists all subdirectories and files in the specified directory using different colors and icons for subdirectories and files")
    print("Usage:")
    print("  " + PurePath(sys.argv[0]).name + " dir_name")

def dir_list(directory, deep):
    '''
    lists all subdirectories and files in the specified directory using different colors 
    and icons for subdirectories and files.
    Args:
        directory (str): path to directory
        deep (int): nesting depth - affects indentation
    '''
    if deep == 0 and Path(directory).is_dir():
        color_print("📂" + str(directory), DIR_COLOR)
        deep += 1

    for path in directory.iterdir():
        if os.path.islink(Path(path)):
            color_print(MARGIN * deep + PurePath(path).name, LINK_COLOR)
        elif Path(path).is_dir():
            color_print(MARGIN * deep + "📂" + PurePath(path).name, DIR_COLOR)
            deep += 1
            path_to_dir = Path(directory).joinpath(PurePath(path).name) # should create the correct path for Windows as well
            #print(deep, path_to_dir)
            dir_list(path_to_dir, deep)
            deep -= 1
        elif Path(path).is_file():
            color_print(MARGIN * deep + "📜" + PurePath(path).name, FILE_COLOR)
        else:
            color_print(MARGIN * deep + PurePath(path).name, Style.RESET_ALL)
        



def main():
    global depth

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

    if not p.exists():
        print("path is not exist")
        sys.exit(2) # No such file or directory
    elif not p.is_dir():
        print("argument must be a directory")
        sys.exit(20) # Not a directory

    dir_list(p, depth)


if __name__ == "__main__":
    main()