import os
import xml.etree.ElementTree as ET
 
def remove_duplicate_log_entries(content):
    # Parse the content into XML elements
    root = ET.fromstring(f"<root>{content}</root>")
    # Use a dictionary to track unique log entries and their counts
    unique_entries = {}
    unique_content = ""
    for entry in root:
        entry_content = entry.text.strip() if entry.text else ""
        if entry_content in unique_entries:
            unique_entries[entry_content] += 1
        else:
            unique_entries[entry_content] = 1
            unique_content += ET.tostring(entry, encoding='unicode')
    # Add duplicate count tags
    for entry_content, count in unique_entries.items():
        if count > 1:
            duplicate_tag = ET.Element("duplicate_count")
            duplicate_tag.text = str(count)
            unique_content = unique_content.replace(f">{entry_content}<", f">{entry_content}<duplicate_count>{count}</duplicate_count><", 1)
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
