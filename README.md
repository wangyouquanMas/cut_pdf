# PDF Page Extractor

This script uses the PyPDF2 library to extract specific page ranges from a PDF file.

# Installation

To run this script, you need to have Python installed. You can download it from the official Python website: Python Downloads

You also need to install the PyPDF2 library. You can install it using pip by running the following command:

pip install PyPDF2

# Usage

To use this script, follow these steps:

Open the script file in a Python editor or IDE.
Modify the pdf_path variable to specify the path of the input PDF file.
Modify the page_ranges list to specify the desired page ranges. Each page range should be specified as a tuple containing the start and end page numbers.
Run the script.

The script will extract the specified page ranges from the input PDF file and create separate output files for each range. The output files will be saved in the same directory as the input PDF file.

After running the script, the paths of the extracted page range files will be printed to the console.

Example

Here's an example of how to use the script:

import os
from PyPDF2 import PdfReader, PdfWriter

# Function to extract a range of pages from a PDF
def extract_pages(reader, start_page, end_page, output_file_path):
    # Create a PdfWriter object
    writer = PdfWriter()

    # Iterate over the specified page range
    for page_num in range(start_page, end_page + 1):
        # Get the page from the PdfReader object
        page = reader.pages[page_num - 1]  # PyPDF2 uses zero-indexed pages

        # Add the page to the PdfWriter object
        writer.add_page(page)

    # Write the extracted pages to the output file
    with open(output_file_path, "wb") as output_pdf:
        writer.write(output_pdf)

# Function to extract multiple ranges of pages from a PDF
def extract_multiple_ranges(file_path, page_ranges):
    # Create a PdfReader object from the input PDF file
    reader = PdfReader(file_path)

    # Initialize a list to store the paths of the extracted page ranges
    output_files = []

    # Iterate over each page range
    for i, page_range in enumerate(page_ranges):
        # Extract the start and end page numbers from the page range tuple
        start_page, end_page = page_range

        # Create the output file name and path based on the index of the page range
        output_file_name = f"extracted_pages_{i+1}.pdf"
        output_file_path = os.path.join(os.path.dirname(file_path), output_file_name)

        # Create the output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Call the extract_pages function to extract the specified page range and write it to the output file
        extract_pages(reader, start_page, end_page, output_file_path)

        # Append the output file path to the list of output files
        output_files.append(output_file_path)

    # Return the list of output file paths
    return output_files

# Specify the page ranges to extract
page_ranges = [(262,280), (256,261), (231,255), (209,230), (198,208), (180,197), (171,179), (147,170)]

# Specify the path of the input PDF file
pdf_path = "C:\\path\\to\\input.pdf"

# Call the extract_multiple_ranges function to extract the specified page ranges
output_files = extract_multiple_ranges(pdf_path, page_ranges)

# Print the paths of the extracted page range files
print(output_files)

License

This project is licensed under the [MIT
