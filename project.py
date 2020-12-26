import extract
import re
from zipfile import ZipFile
import email
import os
import pdf_text

#code for unzip file stat here 

# specifying the zip file name
file_name = "resumes.zip"
filename =  file_name.split(".")
folder_name=filename[0]
folder_names=file_name.split(".")
folder_name=folder_names[0]
file =[]
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    arr =zip.namelist()  #extract file and retuen list
    for i in arr:
        file.append(i)

    zip.extractall()


#code for unzip file end here 

#list all files in filder
all_files = os.listdir(folder_name)   

print(all_files)  
d=''''
shdri.babuji@shriresume.com
Ram1 Kumar
+91 505258222
shri.babuji@shriresume.com
Ram Kumar G/14


'''
import saveTocsv
for i in all_files:
    #file =folder_name+"/"+all_files[i]
    string = pdf_text.pdf_data_text(folder_name,i)
    list = extract.Information_data(string)
    
    if list[0]:
        phone_number=list[0][0]

    if list[1][0]:
        email=list[1][0]

    if list[2][0]:
        name=list[2]
    
    #print(phone_number)
    if list[0]:
        name1=str(name[0])
        email1=str(email)
        print(email1)
        print(name1)
        saveTocsv.SaveCSV(name1,email1,phone_number)

