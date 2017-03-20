from __future__ import division
import json
import sys

transi_dic = {'_starting_tag': {'_ending_tag': '_count'}}
#transition diction has the format as transi_dic = [starting_tag][ending_tag]
transi_pro_dic = {}

 
#construct the transition probability
def transi_occurance_compute(line):
 container = line.split(' ')
 index = 0
 while index < len(container)-1:
  initial_tag = container[index].split('/')
  end_tag = container[index+1].split('/')
  index = index + 1
  if transi_dic.has_key(str(initial_tag[1])) == False:
    transi_dic[str(initial_tag[1])] = {}
    #initialize the count to be 1 
    transi_dic[str(initial_tag[1])]['count'] = 1.0
  else:
    transi_dic[str(initial_tag[1])]['count'] = transi_dic[str(initial_tag[1])]['count'] + 1
    if transi_dic[str(initial_tag[1])].has_key(end_tag[1]) == False:
        transi_dic[str(initial_tag[1])][end_tag[1]] = 1.0
    else:
        transi_dic[str(initial_tag[1])][end_tag[1]] = transi_dic[str(initial_tag[1])][end_tag[1]] + 1



def transition_prob_compute():
  for key,value in transi_dic.items():
    count = 1.0
    transi_pro_dic[key] = {}
    if type(value) is dict:
      for k,v in value.items():
        if value.has_key('count'):
          v = v/value['count']
        if k != 'count':
          transi_pro_dic[key][k] = v




#emission diction has the format as transi_dic = [word][tag]
emission_dic = {'_word': {'_tag': '_count'}}
emission_prob_dic = {}


#construct the emission probability
def emission_occurance_compute(line):
  container = line.split(' ')
  emission_index = 0
  while emission_index < len(container)-1:
    word = container[emission_index].split('/')[0]
    tag = container[emission_index].split('/')[1]
    emission_index = emission_index + 1
    if emission_dic.has_key(str(tag)) == False:
      emission_dic[str(tag)] = {}
      #initialize the count to be 1 
      emission_dic[str(tag)]['count'] = 1.0
      emission_dic[str(tag)][word] = 1.0
    else:
      emission_dic[str(tag)]['count'] = emission_dic[str(tag)]['count'] + 1
      if emission_dic[str(tag)].has_key(word) == False:
        emission_dic[str(tag)][word] = 1.0
      else:
        emission_dic[str(tag)][word] = emission_dic[str(tag)][word] + 1


def emission_prob_compute():
  for key,value in emission_dic.items():
    count = 1.0
    emission_prob_dic[key] = {}
    if type(value) is dict:
      for k,v in value.items():
        if value.has_key('count'):
          v = v/value['count']
          emission_prob_dic[key][k] = v



#Execute the function defined above
with open(sys.argv[1]) as ft:
    for line in ft:
        transi_occurance_compute(line)
        emission_occurance_compute(line)

#call the computation function once for probability 
transition_prob_compute()
emission_prob_compute()


output_json_data = {}
output_json_data['transi_pro_dic'] = transi_pro_dic
output_json_data['emission_prob_dic'] = emission_prob_dic

with open('hmmmodel.txt', 'w') as outfile:
    json.dump(output_json_data,outfile, sort_keys = True, indent = 4,ensure_ascii=False)
outfile.close()