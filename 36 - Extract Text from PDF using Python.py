from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# Download pytesseract from github and install in same file path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

from pdf2image import convert_from_path

pages = convert_from_path(
    "file.pdf",
    dpi=300,
    poppler_path=r"C:\poppler\Library\bin"
)
# Download poppler and make file poppler in 'C' drive and paste library file.

full_text = ""

for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page)
    full_text += f"\n--- Page {i+1} ---\n"
    full_text += text

# Save extracted text
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("✅ OCR completed. Text saved to output.txt")
