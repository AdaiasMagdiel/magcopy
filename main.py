import sys

usage = """\
Usage: magcopy <action> <path/file>

Actions:
    copy   - Copy folder or file to clipboard
    move   - Add folder or file to clipboard to move
    paste  - Paste folder or file from clipboard to current folder or specified folder

Options:
    --clip  - If the command is 'copy' and the object is a file, use this option to copy the file content to system clipboard.
    --help  - Display this usage message.

Note:
    This program does not alter the contents of the system's default clipboard. It maintains its own clipboard for managing copied and moved items.

Example:
    magcopy copy /path/to/source/folder
    magcopy paste /path/to/destination/folder

    magcopy move /path/to/source/file
    magcopy paste /path/to/destination/folder

    magcopy copy /path/to/source/file --clip
"""

if __name__ == "__main__":
    sys.argv = sys.argv[1:]

    clip_flag = "--clip" in sys.argv
    if clip_flag:
        sys.argv.pop(sys.argv.index("--clip"))

    if "--help" in sys.argv or len(sys.argv) == 0:
        print(usage)
        sys.exit(0)

    command = sys.argv.pop(0)
    if command == "copy":
        pass
    elif command == "move":
        pass
    elif command == "paste":
        pass
    else:
        print(
            f"Error: Unknown or invalid command '{command}'. Use 'magcopy --help' to view the usage guide."
        )
        sys.exit(1)
