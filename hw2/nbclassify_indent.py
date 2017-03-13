from __future__ import division
import json
import sys


#initialize four dictionaries for each class
tp_dic = {}  #truthful positive
dp_dic = {}     #deceptive positive
dn_dic = {}     #deceptive negative
tn_dic = {}  #truthful negative

prior_pro = {}

#counter of the word for each categories
total_word_count = [0]
tp_word_count = [0]
dp_word_count = [0]
dn_word_count = [0]
tn_word_count = [0]

#function to split the line and conduct the word count
def word_count_update(str, class_dic, class_word_count):
   array = str.split()
   for str in array:
    class_word_count[0] = class_word_count[0]+1.0
    if class_dic.has_key(str):
        class_dic[str] = class_dic[str]+1.0
    else:
        class_dic[str] = 1.0
   return

def convert_to_percentage(dic, count):
    for key in dic:
        dic[key] = dic[key]/count[0]
    return

def read_in(line,dic):
     (key,val) = line.split(' ', 1 )
     dic[str(key)] = str(val)
   
#reading train-text data in to the dictionary

def text_classification(key):
    class_label = train_label_dic[key].strip()
    review_str = train_text_dic[key]
    if class_label == "truthful positive":
        word_count_update(review_str, tp_dic, tp_word_count)
    else:  
        if class_label == "deceptive positive":
            word_count_update(review_str, dp_dic, dp_word_count)
        else: 
            if class_label == "truthful negative":
                word_count_update(review_str, tn_dic, tn_word_count)
            else:    # grade must D or F
                if class_label == "deceptive negative":
                    word_count_update(review_str, dn_dic, dn_word_count)
                
train_label_dic = {}
train_text_dic = {}

with open(sys.argv[2]) as fl:
    for line in fl:
      read_in(line,train_label_dic)
    
with open(sys.argv[1]) as ft:
    for line in ft:
        read_in(line,train_text_dic)
    

#loop through the train_text_dic for counting words
for key in train_text_dic:
 text_classification(key)


total_word_count[0] = tp_word_count[0]+dp_word_count[0]+dn_word_count[0]+tn_word_count[0]

#convert the dictionaries to probability
convert_to_percentage(tp_dic, tp_word_count)
convert_to_percentage(dp_dic, dp_word_count)
convert_to_percentage(dn_dic, dn_word_count)
convert_to_percentage(tn_dic, tn_word_count)



prior_pro['tp'] = tp_word_count[0]/total_word_count[0]
prior_pro['dp'] = dp_word_count[0]/total_word_count[0]
prior_pro['dn'] = dn_word_count[0]/total_word_count[0]
prior_pro['tn'] = tn_word_count[0]/total_word_count[0]


print total_word_count[0]
print tp_dic
print dp_dic
print dn_dic
print tn_dic
print prior_pro


output_json_data = {}
output_json_data['tp_dic'] = tp_dic
output_json_data['dp_dic'] = dp_dic
output_json_data['dn_dic'] = dn_dic
output_json_data['tn_dic'] = tn_dic
output_json_data['prior_pro'] = prior_pro

with open('nbmodel.txt', 'w') as outfile:
    json.dump(output_json_data,outfile, sort_keys = True, indent = 4,ensure_ascii=False)
outfile.close()