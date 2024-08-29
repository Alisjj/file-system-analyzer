# File System Analyzer

File System Analyzer is a Python-based command-line tool that provides comprehensive analysis of file systems. It traverses directories, collects metadata, identifies duplicates, and generates insightful reports about file usage and distribution.

## Features

- Recursive directory traversal
- Detailed file metadata collection
- File type categorization
- Duplicate file detection
- Total file size calculation
- Largest file identification
- Most common file type analysis

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/alisjjw/file-system-analyzer.git
cd file-system-analyzer
```

## How It Works

- Scan a Directory: python main.py --scan /path/to/directory
- Find Duplicates: python main.py --duplicates /path/to/directory
- Search for Files: python main.py /path/to/directory --search ".pdf" --size-gt 1000