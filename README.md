<img src="./public/images/feather angel icon Interleafing.png" alt="Interlacing for File Processing and Dictionary Management" width="658"/>

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)



## Overview

This repository contains scripts for processing text files, managing a character dictionary, and extracting words from files while handling large datasets efficiently. The main functionalities include splitting files into manageable chunks, updating a character dictionary, and extracting words while ensuring that the output files do not exceed specified line limits.

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Scripts](#scripts)
  - [File Splitting with `split`](#file-splitting-with-split)
  - [Character Dictionary Management](#character-dictionary-management)
  - [Word Extraction and Chunking](#word-extraction-and-chunking)
  - [New Words Processing](#new-words-processing)
- [Considerations for Performance](#considerations-for-performance)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Conclusion](#conclusion)

## Requirements

- Python 3.x
- Git Bash or a Unix-like terminal
- Basic understanding of command-line operations

## Usage

1. **Open Git Bash** and navigate to the directory containing the scripts and necessary folders.
2. Ensure the following folder structure:
   ```
   /your_directory/
   ├── chunky/               # Folder containing input files
   ├── output_chunks/       # Folder for output chunk files
   ├── all_words/           # Folder for storing unique words
   └── chara_here.txt       # Character dictionary file
   ```
3. Run the scripts in the following order:
   - Update the character dictionary and extract words.
   - Process new words against the existing dictionary.
```bash
extract_from_chunky.py
```
```bash
sort_output_chunks.py
```

## Scripts

### File Splitting with `split`

You can split a file into chunks using the `split` command in Git Bash. The basic syntax is:

```bash
split [options] [input_file] [output_file_prefix]
```

**Example Commands**:
- Split a file into 100-line chunks:
  ```bash
  split -l 100 myfile.txt chunk_
  ```
- Split a file into 1MB chunks:
  ```bash
  split -b 1M myfile.txt chunk_
  ```

### Character Dictionary Management

The script updates a character dictionary (`chara_here.txt`) by checking each character in the input files against the existing characters. If a new character is found, it is added to the dictionary.

**Key Function**:
```python
def update_dictionary(input_folder, dictionary_file):
    # Implementation details...
```

### Word Extraction and Chunking

This script extracts words from the input files, treating underscores (`_`) as spaces, and saves them in chunks of 100,000 lines each.

**Key Function**:
```python
def extract_words_and_chunk(input_folder, output_folder):
    # Implementation details...
```

### New Words Processing

This script processes the output chunks to identify new words that are not already in the `all_words` folder. It adds these new words to the folder, ensuring that no file exceeds 150,000 lines.

**Key Function**:
```python
def add_new_words(output_folder, all_words_folder):
    # Implementation details...
```

## Considerations for Performance

- **Memory Management**: The scripts are designed to handle large datasets efficiently by processing files in smaller batches and writing output immediately.
- **Error Handling**: The scripts include error handling to manage file access issues gracefully.
- **Resource Limits**: Monitor system resources while running the scripts, especially on systems with limited memory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgments

- This project uses data from Wikipedia, licensed under the [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/by-sa/3.0/).
- Unicode data and standards are provided by the [Unicode Consortium](https://www.unicode.org/).


## Conclusion

This repository provides a comprehensive solution for managing text files and character dictionaries. The scripts are optimized for performance and designed to handle large datasets effectively. Feel free to modify the scripts to suit your specific needs, and ensure to test them on smaller datasets before scaling up. If you have any questions or need further assistance, please reach out!
