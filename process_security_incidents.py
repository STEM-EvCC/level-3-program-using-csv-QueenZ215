#import csv


#with open('security_incidents.csv', mode='r', encoding='utf-8-sig') as csv_file:
#    reader = csv.reader(csv_file, delimiter=',')
#    incidents = list(reader)

#incidents = incidents[1].append()
#for i,v in enumerate(incidents):
#	print(incidents[i])
#	for i,v in enumerate(incidents[i]):
#		print(v)





import csv

# Specify the input and output file names
input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'

# Read the CSV file
with open(input_file, mode='r', encoding='utf-8-sig') as infile:
    reader = csv.reader(infile)
    incidents = list(reader)

# Add a new column with a default value
new_column_name = 'Status'
default_value = 'Pending'

# Add the new column to the header
header = incidents[0] + [new_column_name]

# Add the new column to each row
rows = [row + [default_value] for row in incidents[1:]]

# Write the modified data to a new CSV file
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Modified data saved to '{output_file}'")