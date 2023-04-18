# Python program to convert .tsv file to .csv file
# importing re library
import re
import glob
import os
import sys

for tsv_file in glob.glob('*.tsv'):
    file_name = os.path.basename(tsv_file)
    with open(tsv_file, 'r') as myfile: 
        with open(f"{file_name}.csv", 'w') as csv_file:
            for line in myfile:
            
                # Replace every tab with comma
                fileContent = re.sub("\t", ",", line)
                
                # Writing into csv file
                csv_file.write(fileContent)

# output
print("Successfully made csv file")