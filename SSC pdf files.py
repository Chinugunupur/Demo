import csv
import pdfplumber
import pandas as pd
pdf_fname = r"C:\Users\Srikant Padhy\Desktop\practicepdf1.pdf"
# pdf = pdfplumber.open(pdf_fname)
# first_page = pdf.pages[0]
# df5 = pd.DataFrame(first_page.extract_table())
# print(df5)
# mytabe = df5.replace('/n','')
# if mytabe[0][0] != '':
#     mytabe[0][0] = ''
#     mytabe.to_csv('sri.csv')
# else:
#     mytabe.to_csv('sri.csv')

# outfile = open('CAWARN-all-pages.csv', 'w')
# outcsv = csv.writer(outfile)
txt = ''
Pdf = pdfplumber.open(pdf_fname)
for page in Pdf.pages:
    table = page.extract_table()
    txt = txt + page.extract_text()
print(table)
print(txt)
txt1 = txt.splitlines(True)
df = pd.DataFrame(table)
mytabe= df.replace('/n',' ')
if mytabe[0][0] != '':
    mytabe[1][0] = txt1[0] + 'status'
    mytabe.to_csv('sri.csv')
else:
    mytabe.to_csv('sri.csv')
