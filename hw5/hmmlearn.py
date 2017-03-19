from __future__ import division
import json
import sys

transi_dic = {'starting_tag': {'ending_tag': 'count'}}
#transition diction has the format as transi_dic = [starting_tag][ending_tag]


   
def line_parsing(line):
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


with open(sys.argv[1]) as ft:
    for line in ft:
        line_parsing(line)



# start_tag = 0
# while start_tag < len(transi_dic):
#   for end_tag in transi_dic[start_tag][]

transi_pro_dic = {}


for key,value in transi_dic.items():
  print (key,value)
  count = 1.0
  transi_pro_dic[key] = {}
  if type(value) is dict:
    for k,v in value.items():
      if value.has_key('count'):
        v = v/value['count']
        if k != 'count':
          transi_pro_dic[key][k] = v

print transi_pro_dic

output_json_data = {}
output_json_data['transi_pro_dic'] = transi_pro_dic

with open('hmmmodel.txt', 'w') as outfile:
    json.dump(output_json_data,outfile, sort_keys = True, indent = 4,ensure_ascii=False)
outfile.close()