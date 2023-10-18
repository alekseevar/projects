from PyPDF2 import PdfReader

file = open("pdf_example.pdf", "rb")

pdf_reader = PdfReader(file)

file = pdf_reader.pages[0]
print(file.extract_text())

