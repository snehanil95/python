import csv

with open('DupsFile', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='unix')
                                