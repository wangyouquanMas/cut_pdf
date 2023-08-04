import os
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(reader, start_page, end_page, output_file_path):
    writer = PdfWriter()
    for page_num in range(start_page, end_page + 1):
        page = reader.pages[page_num - 1]  # PyPDF2 uses zero-indexed pages
        writer.add_page(page)

    with open(output_file_path, "wb") as output_pdf:
        writer.write(output_pdf)

def extract_multiple_ranges(file_path, page_ranges):
    reader = PdfReader(file_path)
    output_files = []
    for i, page_range in enumerate(page_ranges):
        start_page, end_page = page_range
        output_file_name = f"extracted_pages_{i+1}.pdf"
        output_file_path = os.path.join("C:\\Users\\wyq19\\Desktop\\PAZKchapter", output_file_name)
        
        # Create the output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        
        extract_pages(reader, start_page, end_page, output_file_path)
        output_files.append(output_file_path)
    return output_files

page_ranges = [(262,280),(256,261),(231,255),(209,230),(198,208),(180,197),(171,179),(147,170)]

pdf_path = "C:\\Users\\wyq19\\Desktop\\PAZKchapter\\ProofsArgsAndZK111.pdf"
output_files = extract_multiple_ranges(pdf_path, page_ranges)
print(output_files)
