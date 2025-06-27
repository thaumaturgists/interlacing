# Character Sorter README

## Overview

The Character Sorter is a Python script designed to read characters from a specified input file, categorize them by their Unicode script, and then write the sorted characters into separate output files organized by script type. This tool is useful for processing text data that contains a variety of character scripts, allowing for better organization and analysis.

## Features

- **Input Handling**: Reads characters from a specified input file (`chara_here.txt`).
- **Script Detection**: Identifies the Unicode script of each character using predefined ranges.
- **Output Organization**: Creates an output directory (`all_characters`) and organizes characters into subdirectories based on their script.
- **Chunking**: Splits characters into manageable chunks for output, ensuring that no single file exceeds 5KB in size.
- **Error Logging**: Logs errors encountered during file reading and writing to a log file (`character_sorter.log`).

## Requirements

- Python 3.x
- Basic understanding of Unicode and character encoding

## Usage

1. **Prepare Input File**: Create a text file named `chara_here.txt` in the same directory as the script. Populate it with the characters you wish to sort.

2. **Run the Script**: Execute the script using Python. The script will read the characters from the input file, sort them by script, and write the results to the output directory.

   ```bash
   python character_sorter.py
   ```

3. **Check Output**: After execution, check the `all_characters` directory for subdirectories corresponding to each script. Each subdirectory will contain text files with sorted characters.

## Output Structure

- The output directory (`all_characters`) will contain subdirectories named after each detected script (e.g., `Latin`, `Japanese - Hiragana`, etc.).
- Each subdirectory will contain files named in the format `script_part_X.txt`, where `X` is the part number. Each file will contain up to 100 characters per line.

## Error Handling

- Any errors encountered while reading the input file or writing to the output files will be logged in `character_sorter.log`. Check this file for details if the script does not run as expected.

## Example

If the input file contains a mix of Latin, Japanese, and Greek characters, the output will be structured as follows:

```
all_characters/
├── Latin/
│   ├── Latin_part_1.txt
│   └── Latin_part_2.txt
├── Japanese - Hiragana/
│   └── Japanese - Hiragana_part_1.txt
└── Greek/
    └── Greek_part_1.txt
```

## Conclusion

The Character Sorter script is a powerful tool for organizing and processing text data with diverse character sets. By categorizing characters by their Unicode script, it facilitates easier analysis and manipulation of multilingual text.
