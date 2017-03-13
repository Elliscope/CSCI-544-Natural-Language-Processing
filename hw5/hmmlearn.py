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
  else:
    if transi_dic[str(initial_tag[1])].has_key(end_tag[1]) == False:
        transi_dic[str(initial_tag[1])][end_tag[1]] = 1
    else:
        transi_dic[str(initial_tag[1])][end_tag[1]] = transi_dic[str(initial_tag[1])][end_tag[1]] + 1


with open(sys.argv[1]) as ft:
    for line in ft:
        line_parsing(line)

output_json_data = {}
output_json_data['transi_dic'] = transi_dic

with open('hmmmodel.txt', 'w') as outfile:
    json.dump(output_json_data,outfile, sort_keys = True, indent = 4,ensure_ascii=False)
outfile.close()