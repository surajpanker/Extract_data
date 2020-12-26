import PyPDF2

def pdf_data_text(folder_name,filename):
    # pdf file object
    file =folder_name+"/"+filename
    # you can find find the pdf file with complete code in below
    pdfFileObj = open(file, 'rb')
    # pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # number of pages in pdf
    np = (pdfReader.numPages)
    print(np)
    # a page object
    pageObj = pdfReader.getPage(0)
    # extracting text from page.
    # this will print the text you can also save that into String
    string=pageObj.extractText()
    return string


