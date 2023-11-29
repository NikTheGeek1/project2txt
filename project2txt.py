import os
import argparse
from pathlib import Path
import fnmatch

def parse_ignore_list(ignore_file):
    with open(ignore_file, "r") as f:
        ignore_list = [line.strip() for line in f.readlines()]
        print(f"Ignoring {ignore_list}")
    return ignore_list

def export_to_text(file_path, output_dir):
    text_path = output_dir / f"{file_path.stem}.txt"
    with open(file_path, 'r') as original_file, open(text_path, 'w') as text_file:
        text_file.write(f"// Filename: {file_path.name}\n\n")
        text_file.write(original_file.read())
        text_file.write(f"\n// End of {file_path.name}\n\n")
    return text_path

def merge_text_files(text_files, output_path):
    with open(output_path, 'w') as merged_file:
        for text_file in text_files:
            with open(text_file, 'r') as file:
                merged_file.write(file.read() + "\n")

def prepare_ignore_list(ignore_list):
    """Modify ignore patterns to match the entire path."""
    new_ignore_list = []
    for pattern in ignore_list:
        if not pattern.endswith('/'):
            # Add patterns to match both files and directories
            new_ignore_list.append(pattern)
            new_ignore_list.append(pattern + '/')
        else:
            # For patterns already ending with '/', match directories only
            new_ignore_list.append(pattern)

        # Also add patterns to match inside directories
        new_ignore_list.append('*/' + pattern)
        new_ignore_list.append('*/' + pattern + '/')
    return new_ignore_list

def is_ignored(path, ignore_list):
    """Check if the given path matches any of the patterns in the ignore list."""
    for pattern in ignore_list:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def process_directory(directory, ignore_list, output_dir):
    text_files = []
    ignore_list = prepare_ignore_list(ignore_list)
    for root, dirs, files in os.walk(directory, topdown=True):
        dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d), ignore_list)]

        for file in files:
            file_path = Path(root) / file
            if is_ignored(str(file_path), ignore_list):
                continue

            text_path = export_to_text(file_path, output_dir)
            text_files.append(text_path)
    return text_files

def main():
    parser = argparse.ArgumentParser(description="Convert files to text and merge them.")
    parser.add_argument("-d", "--directory", help="Path to the directory.", default=".")
    parser.add_argument("-i", "--ignore", help="Path to the file containing a list of files/directories to ignore.", default=None)
    parser.add_argument("-o", "--output", help="Output directory for text files.", default="./text_output")

    args = parser.parse_args()
    directory = Path(args.directory).resolve()
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)

    if args.ignore:
        ignore_list = parse_ignore_list(args.ignore)
    else:
        ignore_list = []

    text_files = process_directory(directory, ignore_list, output_dir)
    if text_files:
        merge_text_files(text_files, output_dir / "merged_output.txt")
        print(f"Merged text file created at {output_dir / 'merged_output.txt'}")
    else:
        print("No text files created.")

if __name__ == "__main__":
    main()
