import os
import csv

final_concept_rows = []
#final_urlpages_rows = []
#final_mctu_rows = []
#concept_indexes = {}
#urlpages_index = 1

directory_path = os.path.dirname(os.path.realpath(__file__))
students_path = os.path.join(directory_path, 'students_run_2parts')
finalConceptsPath = os.path.join(students_path,'final_Concepts.txt')

print "opening file %s" %finalConceptsPath

f =  open(finalConceptsPath)
try:
	final_concept_csv = csv.writer(open(os.path.join(students_path,'final_Concepts_1.txt'), 'w'), delimiter='\t')
	reader = csv.reader(f, delimiter='\t')
	i = 0
	final_concept_csv.writerow(['ID', 'Tokens', 'TokenCount', 'Frequency','DocFrequency',
		'Perm', 'TokensOrigin', 'FirstPos', 'Distance', 'Folder', 'Old ID'])
	for row in reader:
		# since i = 0 is the header file of the csv and we need
		# we need the object to be more than 4 since then it is going to be a valid object
		if i > 0 and len(row) > 4:
			if row[4] > 20 :
				final_concept_csv.writerow(row)
		i += 1
finally:
	f.close()	



## Go through each of the student's folder
#for student_num in os.listdir(students_path):
#	print "Merging student %s" % student_num
#	concept_id_reassign_map = {}
#	urlpages_id_reassign_map = {}
#	exists_concept = []
#	
#	
#	# Get the paths of files
#	student_path = os.path.join(students_path, student_num)
#	concepts_path = os.path.join(student_path, 'Concepts.txt')
#	urlpages_path = os.path.join(student_path, 'UrlPages.txt')
#	mctu_path = os.path.join(student_path, 'MapConceptToUrl.txt')
#
#	# This folder must contain Concepts.txt, UrlPages.txt, MapConceptToUrl.txt
#	if not (os.path.exists(concepts_path) and os.path.exists(urlpages_path) and
#			os.path.exists(mctu_path)):
#		print 'Skipping ', student_path, ' -- not valid directory.'
#		continue
#
#	# Open the concept file
#	with open(concepts_path) as f:
#		reader = csv.reader(f, delimiter='\t')
#		i = 0
#		
#		# read each row
#		for row in reader:
#			if i > 0 and len(row) > 4:
#				concept_token = row[1]
#			
#				# make sure if we've seen this concept key before, if yes,
#				# we want to just update the concept row instead of inserting a
#				# new one
#				if concept_token in concept_indexes:
#					concept_index = concept_indexes[concept_token]
#					existing_row = final_concept_rows[concept_index]
#					#print row
#					#print existing_row
#					existing_row[3] = int(existing_row[3]) + int(row[3])
#
#					# doc frequency
#					existing_row[4] = int(existing_row[4]) + int(row[4])
#
#					concept_id_reassign_map[row[0]] = concept_index
#					#print existing_row
#				else:
#					# we want to make sure that the concept ID is regenerated
#					# instead of taking in what the student's data in face value
#					# since there could be collisions
#
#					## concept_index = len(concept_indexes)
#					concept_index = len(concept_indexes) 
#					concept_indexes[concept_token] = concept_index 
#					concept_id_reassign_map[row[0]] = concept_index
#
#					dup_row = list(row) # duplicate the row
#					dup_row[0] = str(concept_index) 
#					final_concept_rows.append(dup_row)
#
#			i += 1
#
#
## 	print "Write student %s" % student_num
## 	final_exists_concept_csv = csv.writer(open(os.path.join(student_path,
## 'final_exists.txt'), 'w'), delimiter='\t')
## 	for row in exists_concept:
## 		final_exists_concept_csv.writerow(row)
#
#
#	# Open the urlpages file
#	with open(urlpages_path) as f:
#		reader = csv.reader(f, delimiter='\t')
#		i = 0
#
#		for row in reader:
#
#			# ID regeneration; same with concepts
#			urlpages_id_reassign_map[row[0]] = urlpages_index
#
#			if i > 0 and row[0] != '0':			
#				dup_row = list(row) # duplicate the row
#				dup_row[0] = str(urlpages_index)
#				final_urlpages_rows.append(dup_row)
#
#			i += 1
#			urlpages_index += 1
#
#	# Open the MapConceptToUrl file
#	with open(mctu_path) as f:
#		reader = csv.reader(f, delimiter='\t')
#		i = 0
#
#		for row in reader:
#			# we want to make sure the MapConceptToUrl has the right ID
#			# references since we regenerated them
#			concept_in_map = row[0] in concept_id_reassign_map
#			urlpages_in_map = row[1] in urlpages_id_reassign_map
#
#			if i > 0 and row[0] != '0' and concept_in_map and urlpages_in_map:
#				reassigned_concept_id = concept_id_reassign_map[row[0]]
#				reassigned_urlpages_id = urlpages_id_reassign_map[row[1]]
#				final_mctu_rows.append([reassigned_concept_id, reassigned_urlpages_id])
#			else:
#				pass
#
#			i += 1
#
#
## addConceptRow=[]
## addMapRow = []
## addID= []
#
## # concept_id_reassign_map = {}
## # urlpages_id_reassign_map = {}
#
## # concept_indexes = {}
## # i =0 
## for number in final_concept_rows:
## 	if int(number[4]) > 500:
## 		# print "ID "+number[0]
## 		# print "DocFreq "+number[4]
## 		# print 'yes'
## 		dup_id = number[0]
## 		#concept_id_reassign_map[row[0]] = concept_index
## 		# dup_row = list(number)
## 		# dup_row[0] = str(i)
## 		# print "Dup_id "+dup_id
## 		addID.append(dup_id)
## 		addConceptRow.append(number)
## 		#i += 1
#
#
#
## removeRow=[]
## for number in final_mctu_rows:
## 	if str(number[0]) in addID :
## 		addMapRow.append(number)
#
#
#
#
#
#
## Finally, start writing the merged data to final output files.
#final_concept_csv = csv.writer(open(os.path.join(students_path,
#'final_Concepts.txt'), 'w'), delimiter='\t')
#final_urlpages_csv = csv.writer(open(os.path.join(students_path,
#'final_UrlPages.txt'), 'w'), delimiter='\t')
#final_mctu_csv = csv.writer(open(os.path.join(students_path,
#'final_MapConceptToUrl.txt'), 'w'), delimiter='\t')
#
## Write the column names first
#final_concept_csv.writerow(['ID', 'Tokens', 'TokenCount', 'Frequency',
#'DocFrequency', 'Perm', 'TokensOrigin', 'FirstPos', 'Distance', 'Folder', 'Old ID'])
#final_urlpages_csv.writerow(['ID', 'URL', 'WordCount', 'LastScan', 'Cache'])
#final_mctu_csv.writerow(['ConceptID', 'URLID'])
#
## Write the data.
##for row in addConceptRow:
#for row in final_concept_rows:
#	final_concept_csv.writerow(row)
#
#for row in final_urlpages_rows:
#	final_urlpages_csv.writerow(row)
##for row in addMapRow:
#for row in final_mctu_rows:
#	final_mctu_csv.writerow(row)
