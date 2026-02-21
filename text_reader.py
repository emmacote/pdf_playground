"""
text_reader.py
Purpose: Experiment with extracting data from text inside a pdf file.
Note: Seems to only work assuming the file was OCR-ed in by the scanner
to begin with.

And even OCR scanned come with no guarantee.
There's no guarantee that the OCR embedded in the hardware and/or OS to get everything.

NOTE: 
"""
from PyPDF2 import PdfReader, PageObject
from PIL import Image
import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def lookup_extractable_text(page: PageObject):
    extractable_text = page.extract_text()
    if extractable_text:
        print(f"extracted text...")
        print(extractable_text)
        print(f"length of text found: {len(extractable_text)}")
    else:
        print(f"sorry. No extractable text found in this file. :-(")


def create_image_file(page: PageObject):
    image = page.images[0]
    with open("extracted_image.jpg", "wb") as fp:
        fp.write(image.data)

    print(f"stop point...")


def ocr_scan_extracted_image():
    file_name = "extracted_image.jpg"
    string_data = pytesseract.image_to_string("extracted_image.jpg")
    print(string_data)


if __name__ == '__main__':
    print("welcome to my pdf playground (text extractor script)...")

    if len(sys.argv) > 1:

        file_name = sys.argv[1]
        print(f"working with file: {file_name}")
        reader = PdfReader(file_name)
        print(f"page count: {len(reader.pages)}")
        page = reader.pages[0]

        #lookup_extractable_text(page)
        #create_image_file(page)
        ocr_scan_extracted_image()