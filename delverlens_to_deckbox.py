import csv
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

start_dir = 'C:/Users/kevin/Downloads/'
filenames = askopenfilenames(initialdir = start_dir, title = 'Select file from DelverLens.')
p = Path(filenames[0])
current_dir = str(p.parent) + '/'

header_written = False

with open(current_dir + 'list_export.csv', 'w', newline='') as csvfile2:
	cardwrite = csv.writer(csvfile2, delimiter=',', quotechar='"')
	for filename in filenames:
		with open(filename, newline='') as csvfile:
			cardread = csv.reader(csvfile, delimiter=',', quotechar='"')
#		with open(filename[:-4] + '_fixed.csv', 'w', newline='') as csvfile2:
			
			for row in cardread:
				if row[0] != 'Count':
					# make tradelist count = 0
					row[1] = '0'
					
					# fix some discrepancies in set names
					row[3] = row[3].replace('Timeshifted', '"Timeshifted"')
					row[3] = row[3].replace('Commander 2011', 'Commander')
					row[3] = row[3].replace('Magic 2014', 'Magic 2014 Core Set')
					#row[3] = row[3].replace('Magic 2015', 'Magic 2015 Core Set')
					row[3] = row[3].replace('Modern Masters 2015', 'Modern Masters 2015 Edition')
					row[3] = row[3].replace('Modern Masters 2017', 'Modern Masters 2017 Edition')
					
					# set quality if empty
					if row[5] == '':
						row[5] = 'Near Mint'
					
					# set language if empty
					if row[6] == '':
						row[6] = 'English'
					
					# custom tag for signed, move into correct column
					row[8] = row.pop(-1)
					
					del(row[-1])
					
					# write to csv file
					cardwrite.writerow(row)
					
				elif not(header_written):
					cardwrite.writerow(row)
					header_written = True