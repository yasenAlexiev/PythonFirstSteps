import csv
import PyPDF2
import re

# PDFs and Spreadsheets Puzzle Exercise

# Task One: Use Python to extract the Google Drive link from the .csv file.
# (Hint: Its along the diagonal from top left to bottom right).

f = open("find_the_link.csv", encoding="utf-8")
csv_data = csv.reader(f)
data_lines = list(csv_data)

row_number = len(data_lines)
col_number = len(data_lines[0])

link = ''
if row_number == col_number:
    for i in range(row_number):
        link += data_lines[i][i]

print(link)

pdf_file = open("Find_the_Phone_Number.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)
pages_in_document = len(pdf_reader.pages)

for num_page in range(pages_in_document):
    match = re.findall(r"\d{3}.{1}\d{3}.{1}\d{4}", pdf_reader.pages[num_page].extract_text())
    if match:
        print(match)



