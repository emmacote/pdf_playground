"""
text_reader.py
Purpose: Experiment with extracting data from text inside a pdf file.
Note: Seems to only work assuming the file was OCR-ed in by the scanner
to begin with.

And even OCR scanned come with no guarantee.
There's no guarantee that the OCR embedded in the hardware and/or OS to get everything.
"""
from PyPDF2 import PdfReader
import sys



if __name__ == '__main__':
    print("welcome to my pdf playground (text extractor script)...")
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print(f"working with file: {file_name}")
        reader = PdfReader(file_name)
        print(f"page count: {len(reader.pages)}")
        page = reader.pages[0]

        extractable_text = page.extract_text()
        if extractable_text:
            print(f"extracted text...")
            print(extractable_text)
            print(f"length of text found: {len(extractable_text)}")
        else:
            print(f"sorry. No extractable text found in this file. :-(")
