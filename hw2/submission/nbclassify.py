from __future__ import division
from collections import OrderedDict
import json
import sys
import math
from pprint import pprint


#function to compute the probability of belong to class
def prob_compute(input,class_dic,prior_pro):
   array = input.split()
   output_prob = math.log(prior_pro)
   for str in array:
   	if class_dic.has_key(str):
   			output_prob = output_prob + math.log(class_dic[str])
   return output_prob
  
#import the nbmodel.txt data
with open('nbmodel.txt') as data_file:  
    data = json.load(data_file)

#read the test-text.txt file in
test_text_dic = OrderedDict()
with open(sys.argv[1]) as ft:
	for line in ft:
		(key,val) = line.split(' ', 1 )
		test_text_dic[str(key)] = str(val)

result_labels_dic = OrderedDict()


#loop through the review text and compute the NB probability result
for key in test_text_dic:
	ps_prob = prob_compute(test_text_dic[key], data['ps_dic'], data['prior_pro']['ps'])
	ng_prob = prob_compute(test_text_dic[key], data['ng_dic'], data['prior_pro']['ng'])
	tr_prob = prob_compute(test_text_dic[key], data['tr_dic'], data['prior_pro']['tr'])
	de_prob = prob_compute(test_text_dic[key], data['de_dic'], data['prior_pro']['de'])
	first = max(tr_prob,de_prob)
	second = max(ps_prob,ng_prob)

	first_result = ""
	second_result = ""

	if first == tr_prob:
		first_result = "truthful"
	else:
		first_result = "deceptive"

	if second == ps_prob:
		second_result = "positive"
	else:
		second_result = "negative"
    
	result = first_result + " "+second_result
	result_labels_dic[key] = result


#write out to the designated file
fileObject = open("nboutput.txt", "wb")
for key in result_labels_dic:
	fileObject.write(key + " " + result_labels_dic[key] + "\n")
fileObject.close()