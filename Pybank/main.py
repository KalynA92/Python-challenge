import os
import csv


budget_data_csv=os.path.join("Resources", "budget_data.csv")


text_path="output.txt"


with open('budget_data_csv') as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    csv_header=next(csvreader)
    print(f"csv Header: {csv_header}")
    
    for row in csvreader:
        print(row)



        

       

        



