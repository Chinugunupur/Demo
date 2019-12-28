import pdfplumber
import pandas as pd
import re
pdf_fname = r"C:\Users\Srikant Padhy\Desktop\practicepdflic.pdf"
txt = ''
df = pd.DataFrame()
Pdf = pdfplumber.open(pdf_fname)
for page in Pdf.pages:
    table = page.extract_table()
    txt = txt + page.extract_text()
# print(table)
# print(txt)
txt2 =txt.splitlines()
for txt1 in txt2:
    s = re.match('.*[0-9]\s+hours',txt1)
    if s:
        sri = s.group()
        s = sri.__contains__('LIC')
        if s == True:
            pass


