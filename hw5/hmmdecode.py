from __future__ import division
from collections import OrderedDict
import json
import sys
import math
from pprint import pprint
import collections

#function to compute the probability of belong to class
# def prob_compute(input,class_dic,prior_pro):
#    array = input.split()
#    output_prob = math.log(prior_pro)
#    for str in array:
#     if class_dic.has_key(str):
#         output_prob = output_prob + math.log(class_dic[str])
#    return output_prob
  
#import the nbmodel.txt data


#function to parse the input line
Final_Prob = 0
Ptemp = 1
Prob = 1;

# def viterbiAlgorithm(line,index,probability,prev_tag):
  # word = line[index]
  # if index == len(line):
  #   return Final_Prob
  # for key in emission_prob_dic[word]:
  #   if transi_prob_dic[prev_tag].has_key(key):
  #     Prob = Ptemp + math.log(emission_prob_dic[word][key]) + math.log(transi_prob_dic[prev_tag][key])

  #   Ptemp = Prob


#viterbi algorithm returns the probability
# def viterbiAlgorithm(line, index):
#   if index == 0:
#     return 1

def line_parsing(line):
  input_array = line.split(' ')
  tag_array = []




with open('hmmmodel.txt') as data_file:  
    data = json.load(data_file)

emission_prob_dic = collections.OrderedDict(data['emission_prob_dic'])
transi_pro_dic = collections.OrderedDict(data['transi_pro_dic'])

print transi_pro_dic.keys()
print len(transi_pro_dic.keys())

result_labels_dic = OrderedDict()




#loop through the review text and compute the NB probability result
# for key in test_text_dic:
#   ps_prob = prob_compute(test_text_dic[key], data['ps_dic'], data['prior_pro']['ps'])
#   ng_prob = prob_compute(test_text_dic[key], data['ng_dic'], data['prior_pro']['ng'])
#   tr_prob = prob_compute(test_text_dic[key], data['tr_dic'], data['prior_pro']['tr'])
#   de_prob = prob_compute(test_text_dic[key], data['de_dic'], data['prior_pro']['de'])
#   first = max(tr_prob,de_prob)
#   second = max(ps_prob,ng_prob)

#   first_result = ""
#   second_result = ""

#   if first == tr_prob:
#     first_result = "truthful"
#   else:
#     first_result = "deceptive"

#   if second == ps_prob:
#     second_result = "positive"
#   else:
#     second_result = "negative"
    
#   result = first_result + " "+second_result
#   result_labels_dic[key] = result


#write out to the designated file
fileObject = open("nboutput.txt", "wb")
for key in result_labels_dic:
  fileObject.write(key + " " + result_labels_dic[key] + "\n")
fileObject.close()