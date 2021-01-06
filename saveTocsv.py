# writing to CSV 
import csv 
	
# field names 

# writing the fields 
# 
# 
def SaveCSV(name,email,phone):
	# name of csv file
	filename="data.csv" 
	file = open(filename, 'w', newline ='') 
	with file: 
		# identifying header  
		fields = ['Name','Email', 'PhoneNumber'] 
		writer = csv.DictWriter(file, fieldnames = fields) 
		# writing data row-wise into the csv file 
		writer.writerow({'Name' : name,'Email': email,'PhoneNumber': phone }) 
