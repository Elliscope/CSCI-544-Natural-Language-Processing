from __future__ import division
from collections import OrderedDict
import json
import sys
import math

#import the nbmodel.txt data
from pprint import pprint

with open('nbmodel.txt') as data_file:  
    data = json.load(data_file)

#pprint(data['prior_pro'])

#function to compute the probability of belong to class
def prob_compute(input,class_dic,prior_pro):
   array = input.split()
   output_prob = prior_pro
   for str in array:
   	if class_dic.has_key(str):
   		if(class_dic[str]!=0):
   			output_prob = output_prob + class_dic[str]
   # print "here is the output_prob"
   # print output_prob
   return output_prob


#read the test-text.txt file in
test_text_dic = OrderedDict()
with open(sys.argv[1]) as ft:
	for line in ft:
		(key,val) = line.split(' ', 1 )
		test_text_dic[str(key)] = str(val)

result_labels_dic = OrderedDict()


#loop through the review text and compute the NB probability result
for key in test_text_dic:
	tp_prob = prob_compute(test_text_dic[key], data['tp_dic'], data['prior_pro']['tp'])
	dp_prob = prob_compute(test_text_dic[key], data['dp_dic'], data['prior_pro']['dp'])
	tn_prob = prob_compute(test_text_dic[key], data['tn_dic'], data['prior_pro']['tn'])
	dn_prob = prob_compute(test_text_dic[key], data['dn_dic'], data['prior_pro']['dn'])
	result = max(tp_prob,dp_prob,tn_prob,dn_prob)
	print "This is the result", result
	print "truthful negative",tn_prob
	print "truthful positive",tp_prob
	print "deceptive positive",dp_prob
	print "deceptive negative",dn_prob  
	if result == tn_prob:
		result_labels_dic[key] = 'truthful negative'    
	if result == tp_prob:
		result_labels_dic[key] = 'truthful positive'
	if result == dp_prob:
		result_labels_dic[key] = 'deceptive positive'
	if result == dn_prob:
		result_labels_dic[key] = 'deceptive negative'
	print result_labels_dic[key]


#write out to the designated file
fileObject = open("nboutput.txt", "wb")
for key in result_labels_dic:
	fileObject.write(key + " " + result_labels_dic[key] + "\n")
fileObject.close()