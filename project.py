import extract
import re
from zipfile import ZipFile
import email
import os
import pdf_text
import name
#code for unzip file stat here 

# specifying the zip file name
file_name = "ready.zip"

# opening the zip file in READ mode
file=[]
with ZipFile('ready.zip', 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    arr =zip.namelist()  #extract file and retuen list
    for i in arr:
        file.append(i)

    zip.extractall('./filefolder')


#code for unzip file end here 
folder_name="filefolder"
#list all files in filder
all_files = os.listdir(folder_name)   

#print(all_files) 

#demo string 
d=''''
shdri.babuji@shriresume.com
Ram1 Kumar
+91 505258222
shri.babuji@shriresume.com
Ram Kumar G/14


'''
import csv
data=[]
for i in all_files:
    #file =folder_name+"/"+all_files[i]
  
    string =(pdf_text.convert_pdf_to_txt(i))
    name1=name.extract_names(i)
    email1,phone1=extract.Information_data(string)
    print(name1,email1,phone1)
    data.append([name1,email1,phone1])
    


  
# opening the csv file in 'a+' mode 
file = open('data.csv', 'a+', newline ='') 
  
# writing the data into the file 
with file:     
    write = csv.writer(file) 
    write.writerows(data) 