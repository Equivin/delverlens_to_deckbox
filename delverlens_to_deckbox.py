import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(initialdir = './', title = 'Select file from DelverLens.')

with open(filename, newline='') as csvfile:
	cardread = csv.reader(csvfile, delimiter=',', quotechar='"')
	with open(filename[:-4] + '_fixed.csv', 'w', newline='') as csvfile2:
		cardwrite = csv.writer(csvfile2, delimiter=',', quotechar='"')
		for row in cardread:
			if row[0] != 'Count':
				# make tradelist count = 0
				row[1] = '0'
				
				# fix some discrepancies in set names
				row[3] = row[3].replace('Timeshifted', '"Timeshifted"')
				row[3] = row[3].replace('Commander 2011', 'Commander')
				row[3] = row[3].replace('Magic 2014', 'Magic 2014 Core Set')
				row[3] = row[3].replace('Magic 2015', 'Magic 2015 Core Set')
				
				# set quality if empty
				if row[5] == '':
					row[5] = 'Near Mint'
				
				# set language if empty
				if row[6] == '':
					row[6] = 'English'
				
				# custom tag for signed, move into correct column
				row[8] = row.pop(-1)
			
			# write to csv file
			cardwrite.writerow(row)