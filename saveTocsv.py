# writing to CSV 
import csv 
	
# field names 
fields = ['Name','Email', 'Phone Number'] 
# name of csv file 
filename = "data.csv"
		
# writing the fields 
def SaveCSV(name,email,phone):
	with open(filename, 'w') as csvfile: 
		# creating a csv writer object 
		csvwriter = csv.writer(csvfile) 
		csvwriter.writerow(fields) 	

		#field = [nameemailphone] 

		# writing the data rows 
		vv =[name,email,phone]
		csvwriter.writerow(vv) 
		
		print("Data has been written")
