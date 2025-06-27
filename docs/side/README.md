# Interlacing for File Processing and Dictionary Management

A lightweight Python library designed to streamline the interleaving of multiple file streams and provide robust dictionary‐based data management utilities. Perfect for log aggregation, CSV/JSON mashups, and any workflow where you need to weave together file contents and maintain in‐memory lookups.

---

## Table of Contents

1. [Features](#features)  
2. [Getting Started](#getting-started)  
3. [Installation](#installation)  
4. [Basic Usage](#basic-usage)  
   - [Interlacing Files](#interlacing-files)  
   - [Merging Dictionaries](#merging-dictionaries)  
   - [Splitting Dictionaries](#splitting-dictionaries)  
   - [Streamed Processing](#streamed-processing)  
5. [API Reference](#api-reference)  
6. [Examples](#examples)  
7. [Project Structure](#project-structure)  
8. [Contributing](#contributing)  
9. [License](#license)  

---

## Features

- **Interlace multiple file streams** line-by-line or chunk-wise  
- **Thread-safe dictionary merging** with custom conflict resolution  
- **Split large dictionaries** into balanced shards for parallel processing  
- **Lazy/streamed processing** to handle gigabyte-scale files with constant memory  
- **Built-in support** for CSV, JSON, plain text, and binary file formats  

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+  
- Optional: `aiofiles` for async file interlacing  
- Optional: `pandas` for advanced CSV handling  

---

## Installation

```bash
pip install interlace-fpm
```

Or clone and install from source:

```bash
git clone https://github.com/your-username/interlace-fpm.git
cd interlace-fpm
pip install .
```

---

## Basic Usage

### Interlacing Files

```python
from interlace_fpm import interlace_files

# Merge two log files by alternating lines
for line in interlace_files(['server1.log', 'server2.log']):
    print(line.strip())
```

### Merging Dictionaries

```python
from interlace_fpm import merge_dicts

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}

# By default, values from later dicts overwrite earlier ones
merged = merge_dicts(dict_a, dict_b)
# merged == {'a':1, 'b':3, 'c':4}
```

You can supply a custom resolver:

```python
def sum_resolver(key, old, new):
    return old + new

merged_sum = merge_dicts(dict_a, dict_b, resolver=sum_resolver)
# merged_sum == {'a':1, 'b':5, 'c':4}
```

### Splitting Dictionaries

```python
from interlace_fpm import split_dict

large_dict = {i: i*i for i in range(1000)}
shards = split_dict(large_dict, 4)
# shards is a list of 4 smaller dicts, each ~250 items
```

### Streamed Processing

Process massive logs without loading entire file into memory:

```python
from interlace_fpm import stream_dict_updates

# Yields updated dict state as you read each chunk
for partial_dict in stream_dict_updates('bigfile.json', chunk_size=1024):
    process(partial_dict)
```

---

## API Reference

#### interlace_files(file_paths: List[str], chunk: bool = False) → Iterator[str]  
Read lines (or chunks, if `chunk=True`) alternately from each file.

#### merge_dicts(*dicts: Dict, resolver: Callable = None) → Dict  
Merge multiple dictionaries. If `resolver` is provided, it dictates how to resolve key collisions.

#### split_dict(d: Dict, parts: int) → List[Dict]  
Split one dictionary into `parts` roughly equal-sized dictionaries.

#### stream_dict_updates(file_path: str, chunk_size: int) → Iterator[Dict]  
Yield dictionary updates as the file is read in chunks.

---

## Examples

See the [examples](examples/) folder for ready-to-run scripts:

- **log_merger.py**: Interlace multiple server logs and write to `combined.log`.  
- **csv_json_mashup.py**: Read a CSV and a JSON file in parallel, merge rows by key.  
- **dict_sharder.py**: Split a million-entry dictionary into 10 shards for multiprocessing.  

---

## Project Structure

```
interlace-fpm/
├── interlace_fpm/
│   ├── __init__.py
│   ├── file_interlacer.py
│   ├── dict_utils.py
│   └── stream_processor.py
├── examples/
│   ├── log_merger.py
│   └── csv_json_mashup.py
├── tests/
│   ├── test_file_interlacer.py
│   └── test_dict_utils.py
├── LICENSE
└── README.md
```

---

## Contributing

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m 'Add some feature'`)  
4. Push to the branch (`git push origin feature/YourFeature`)  
5. Open a pull request  

Please follow the PEP8 style guide and include unit tests for new functionality.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Next Steps You Might Explore**  
- Performance benchmarks using large binary files  
- Async interlacing with `asyncio` and `aiofiles`  
- Integrating with CI/CD (GitHub Actions) for automated testing and publishing  
- Packaging as a Docker container for language-agnostic deployments
