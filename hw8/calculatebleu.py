from __future__ import division
import json
import sys
import re
import os
import numpy as np
import math



print sys.argv[1]
print sys.argv[2]

candidate_data = []
reference_data = {}
reference_data_indexed = {}

ref_dic = []

ref_sentence_lengh_dic = {}
candi_sentence_lengh_array = []
best_match_length_array = []


def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

#Function to compute the P value
def getBLEUvalue(candidate_array,reference_data,BP):
	BLEU = 0
	for i in range(1,5):
		print "HERE IS A I VALUE", i
		Pvalue = getPvalue(candidate_data,reference_data,i)/candiCount(candi_sentence_lengh_array,i)
		#print candiCount(candi_sentence_lengh_array,i)
		BLEU = BLEU + 1/4 * math.log(Pvalue)
	BLEU = BP * math.exp(BLEU)
	return BLEU


def getPvalue(candidate_data,reference_data,number):
	Pcount = 0
	for i in range(0,len(candidate_data)):
		Pcount = Pcount + matchCount(candidate_data[i],reference_data_indexed[i],number)
		#print "Pcount", Pcount
	return Pcount

#Function to get the match count for one sentence 
def matchCount(candidate,reference_list,number):
	refer_sen_dic = {}
	match_count = 0

	candidate_sentence = candidate.split(" ")
	candidate_string_chain = [" ".join(candidate_sentence[i:i+number]) for i in range(0, len(candidate_sentence)-number)]
	
	for reference_sentence_string in reference_list:
		reference_sentence = reference_sentence_string.split(" ")
		reference_string_chain = [" ".join(reference_sentence[i:i+number]) for i in range(0, len(reference_sentence)-number)]
		for word_chain in reference_string_chain:
			refer_sen_dic[word_chain] = 1

	#Go through the refer_sen_dic to count the number of matches
	for candi_seg_chain in candidate_string_chain:
		if candi_seg_chain in refer_sen_dic:
			match_count += 1

	#print "match count ", match_count
	#print "refer_sen_dic",refer_sen_dic
	#print "candidate_string_chain", candidate_string_chain
	return match_count

def candiCount(candidate_array,number):
	return sum(candidate_array) + (number-1)*len(candidate_array)

#load the candidate file into array by sentence
with open(sys.argv[1]) as fl:
	text = fl.read()
	candidate_data = re.split(r' *[\.\?!:][\'"\)\]]* *', text)
    
#print candidate_data



#load the reference file into a dictionry
reference_file = os.listdir(sys.argv[2])
ref_index = 0
for file_name in reference_file:
	with open(sys.argv[2]+file_name) as fd:
		text = fd.read()
		reference_data[ref_index] = re.split(r' *[\.\?!:][\'"\)\]]* *', text)
		ref_index = ref_index + 1 

# print reference_file
# print reference_data


#Compute the BP score

#Compute the C value
for line in candidate_data:
	word_array = line.split(' ')
	candi_sentence_lengh_array.append(len(word_array))
#print candi_sentence_lengh_array


#Compute the R value
for key, value in reference_data.iteritems():
	ref_length_index = 0
	for line in value:
		word_array = line.split(' ')
		if ref_length_index in ref_sentence_lengh_dic:
			ref_sentence_lengh_dic[ref_length_index].append(len(word_array))
			reference_data_indexed[ref_length_index].append(line)
		else:
			ref_sentence_lengh_dic[ref_length_index] = []
			reference_data_indexed[ref_length_index] = []
			ref_sentence_lengh_dic[ref_length_index].append(len(word_array))
			reference_data_indexed[ref_length_index].append(line)
		ref_length_index = ref_length_index+1

#print ref_sentence_lengh_dic
#print reference_data_indexed

#find the best match with the above arrays
for k in range(0,len(candi_sentence_lengh_array)):
	candi_len = candi_sentence_lengh_array[k]
	best_match_length_array.append(min(ref_sentence_lengh_dic[k], key=lambda x:abs(x-candi_len)))

#print best_match_length_array


r = sum(best_match_length_array)
c = sum(candi_sentence_lengh_array)

# print c
# print r

#Compute the BP according to the condition
if c>=r:
	BP = 1
else:
	BP = math.exp(1-r/c)

print BP


print getBLEUvalue(candidate_data,reference_data,BP)






#write tou the float point to the following file
#bleu_out.txt