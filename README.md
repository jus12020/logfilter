# LogFilter

LogFilter is a lightweight log filtering tool built with Python. It processes log files by removing duplicate log entries.

## Features

- Lightweight log filtering
- Removes duplicate log entries

## Requirements

- Python 3.6 or higher


## To Do

- Track number of duplicates
- This feature may be implemented using dictionaries 

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/jus12020/logfilter.git
    cd logfilter
    ```

## Usage

1. Run the script:
    ```sh
    python logfilter.py
    ```

2. The script will process all `.log` files in the current directory, remove duplicate log entries, and create new files with 'two' appended to the original filenames.

## Example Script

Here's the main script used for processing log files:

```python
import os
import xml.etree.ElementTree as ET

def remove_duplicate_log_entries(content):
    # Parse the content into XML elements
    root = ET.fromstring(f"<root>{content}</root>")
    
    # Use a set to track unique log entries based on their content
    unique_entries = set()
    unique_content = ""
    
    for entry in root:
        entry_content = entry.text.strip() if entry.text else ""
        if entry_content not in unique_entries:
            unique_entries.add(entry_content)
            unique_content += ET.tostring(entry, encoding='unicode')
    
    return unique_content

def process_log_files():
    # Get the current directory
    current_directory = os.getcwd()
    
    # Iterate over all files in the directory
    for filename in os.listdir(current_directory):
        # Check if the file is a .log file
        if filename.endswith('.log'):
            # Read the content of the .log file
            with open(filename, 'r') as file:
                content = file.read()
            
            # Remove duplicate log entries from the content
            content = remove_duplicate_log_entries(content)
            
            # Create a new filename with 'two' appended to the original filename
            new_filename = filename.replace('.log', 'two.log')
            
            # Write the content to the new file
            with open(new_filename, 'w') as new_file:
                new_file.write(content)
    
    print("Processing complete. New files have been created with 'two' appended to the filenames.")

if __name__ == "__main__":
    process_log_files()
