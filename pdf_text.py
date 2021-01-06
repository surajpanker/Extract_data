from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(pat):
    folder_name1="filefolder"
    path=folder_name1+'./'+pat
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text







'''
import saveTocsv
for i in all_files:
    #file =folder_name+"/"+all_files[i]
    string = pdf_text.pdf_data_text(folder_name,i)
    list = extract.Information_data(string)
    #print(list)
    # if list[0]:
    #     phone_number=list[0][0]

    # if list[1][0]:
    #     email=list[1][0]

    # if list[2][0]:
    #     name=list[2]
    
    # #print(phone_number)
    # if list[0]:
    #     name1=str(name[0])
    #     email1=str(email)
    #     print(email1)
    #     print(name1)
    #     saveTocsv.SaveCSV(name1,email1,phone_number)

'''