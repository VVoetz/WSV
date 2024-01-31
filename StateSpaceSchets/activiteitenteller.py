import csv
import math

# Specify the path to your CSV file
csv_file_path = 'data/vakken.csv'

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    next(csv_reader)
    totaal = 0
    # Iterate over each row in the CSV file
    for row in csv_reader:
        activiteit = 0

        # voegt hoorcolleges toe
        if row[1] != '':
            activiteit += int(row[1])

        # voegt werkcolleges toe
        if row[3] == '':
            if row[2] != '':
                activiteit += int(row[2])
        else:
            if row[2] != '':
                activiteit += int(row[2]) * math.ceil(int(row[6]) / int(row[3]))

        # voegt practica toe 
        if row[5] == '':
            if row[4] != '':
                activiteit += int(row[4])
        else:
            if row[4] != '':
                activiteit += int(row[4]) * math.ceil(int(row[6]) / int(row[5]) )
        
        print(f"{row[0]}:  {str(activiteit)}")  
        totaal += activiteit
    print(f"totaal: {totaal}")  
