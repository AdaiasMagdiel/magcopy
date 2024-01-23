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

Certainly! Below is an additional section for testing using `pytest` in your README:

## Testing

To run the tests for `magcopy`, you need to have `pytest` installed. If you don't have it installed, you can install it using the following command:

```bash
pip install pytest
```

Once `pytest` is installed, you can run the tests by executing the following command in the root directory of your project:

```bash
pytest
```

This will discover and run all the test files in your project. Make sure you have the required dependencies and a proper Python environment set up before running the tests.

### Running Specific Tests

If you want to run tests from a specific file or directory, you can provide the file or directory path as an argument to `pytest`. For example:

```bash
pytest tests/test_clipboard.py
```

This command will run only the tests defined in the `test_clipboard.py` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
