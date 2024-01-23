# magcopy

`magcopy` is a command-line utility that simplifies the copy and move operations of files and directories between terminal windows. It allows users to copy from one terminal and paste into another with ease. The utility is designed to be used in a terminal environment and maintains its own clipboard for managing copied and moved items.

## Installation

You can install `magcopy` using the following command:

```bash
pip install magcopy
```

## Usage

```bash
magcopy <action> <path/file> [--clip] [--help]
```

### Actions

- **copy**: Copy a folder or file to the clipboard.
- **move**: Add a folder or file to the clipboard for moving.
- **paste**: Paste a folder or file from the clipboard to the current folder or a specified folder.

### Options

- `--clip`: If the command is 'copy' and the object is a file, use this option to copy the file content to the system clipboard.
- `--help`: Display the usage message.

### Examples

```bash
magcopy copy /path/to/source/folder
magcopy paste /path/to/destination/folder

magcopy move /path/to/source/file
magcopy paste /path/to/destination/folder

magcopy copy /path/to/source/file --clip
```

## Notes

- This program does not alter the contents of the system's default clipboard. It maintains its own clipboard for managing copied and moved items.

## Error Handling

In case of errors, the utility provides clear error messages to guide the user.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
