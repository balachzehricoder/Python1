from pdf2docx import Converter

pdf_file = 'i.pdf'
docx_file= 'i.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()