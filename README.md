# Directory to TXT Converter

This script is designed to convert files within a specified directory into individual TXTs and then merge them into a single TXT file. It's useful for creating a compiled document from multiple files, while also providing the functionality to ignore specific files or directories.

## Features

- Converts each file in a directory to a separate TXT.
- Merges all generated TXTs into a single TXT file.
- Option to ignore specific files or directories during the conversion process.

## Usage

To use the script, you need to provide the directory containing the files you want to convert. Optionally, you can specify a file containing a list of items to ignore and an output directory for the generated TXTs.

## Command Line Arguments

- `-d` or `--directory`: The path to the directory containing the files to be converted. Default is the current directory.
- `-i` or `--ignore`: Path to a file containing a list of files/directories to ignore.
- `-o` or `--output`: The output directory for the TXT files. Default is ./TXT_output.

## Example

```bash
python script_name.py -d /path/to/directory -i /path/to/ignorelist.txt -o /path/to/output
```

This command will process files in /path/to/directory, ignoring files listed in /path/to/ignorelist.txt, and will save the output in /path/to/output.

## Output
The script will create individual TXTs for each file in the specified directory (excluding ignored items) and then merge these TXTs into a single file named `merged_output.TXT` in the specified output directory.

## Note

- The `export_to_TXT` function in the script creates basic TXTs with the file name as content. Depending on the nature of your files, you may need to modify this function to better suit your conversion needs.