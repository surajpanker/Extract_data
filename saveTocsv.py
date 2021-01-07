# writing to CSV 
import csv 
	
# field names 

# writing the fields 
# 
# 
def SaveCSV(first,last,email,phone):
	# name of csv file
	filename="data.csv" 
	file = open(filename, 'w', newline ='') 
	with file: 
		# identifying header  
		fields = ['First Name' ,'Second Name' ,'Phone Number' ,'Email'] 
		writer = csv.DictWriter(file, fieldnames = fields) 
		# writing data row-wise into the csv file 
		writer.writerow({'First Name':first,'Second Name':last,'Phone Number':phone ,'Email':email}) 
   



