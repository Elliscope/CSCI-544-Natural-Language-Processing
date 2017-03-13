from __future__ import division
import json
import sys


#initialize four dictionaries for each class
# tp_dic = {}  #truthful positive
# dp_dic = {}     #deceptive positive
# dn_dic = {}     #deceptive negative
# tn_dic = {}  #truthful negative
dic = {}
prior_pro = {}

ps_dic = {}
ng_dic = {}
tr_dic = {}
de_dic = {}

#counter of the word for each categories
total_word_count = [0]

ps_word_count = [0]
ng_word_count = [0]
tr_word_count = [0]
de_word_count = [0]

total_review_count = [0]

ps_review_count = [0]
ng_review_count = [0]
tr_review_count = [0]
de_review_count = [0]

#function to split the line and conduct the word count
def word_count_update(str, class_dic, class_word_count,class_review_count):
   array = str.split()
   class_review_count[0] = class_review_count[0]+1.0
   total_review_count[0] = total_review_count[0]+1.0
   for str in array:
    class_word_count[0] = class_word_count[0]+1.0
    if class_dic.has_key(str):
        class_dic[str] = class_dic[str]+1.0
    else:
        class_dic[str] = 2.0
        class_word_count[0] = class_word_count[0]+1.0
        dic[str] = 1.0
   return

def convert_to_percentage(dic, count):
    for key in dic:
        dic[key] = dic[key]/count[0]
    return

def read_in_label(line,dic):
     (key,val) = line.split(' ', 1 )
     binary_class = val.split()
     binary_dic = {}
     binary_dic[binary_class[0]] = 1
     binary_dic[binary_class[1]] = 1
     dic[str(key)] = binary_dic

def read_in_text(line,dic):
     (key,val) = line.split(' ', 1 )
     dic[str(key)] = str(val)


#reading train-text data in to the dictionary

def text_classification(key):
    class_label = train_label_dic[key]
    review_str = train_text_dic[key]
    if class_label.has_key("positive"):
        word_count_update(review_str, ps_dic, ps_word_count,ps_review_count)
    if class_label.has_key("negative"):
        word_count_update(review_str, ng_dic, ng_word_count,ng_review_count)
    if class_label.has_key("truthful"):
        word_count_update(review_str, tr_dic, tr_word_count,tr_review_count)
    if class_label.has_key("deceptive"):
        word_count_update(review_str, de_dic, de_word_count,de_review_count)
                
train_label_dic = {}
train_text_dic = {}

with open(sys.argv[2]) as fl:
    for line in fl:
      read_in_label(line,train_label_dic)
    
with open(sys.argv[1]) as ft:
    for line in ft:
        read_in_text(line,train_text_dic)
    

#loop through the train_text_dic for counting words
for key in train_text_dic:
 text_classification(key)


#smoothing
for key in dic:
 if ps_dic.has_key(key)==False:
  ps_dic[key]=1.0
  ps_word_count[0]=ps_word_count[0]+1.0
 if ng_dic.has_key(key)==False:
  ng_dic[key]=1.0
  ng_word_count[0]=ng_word_count[0]+1.0
 if tr_dic.has_key(key)==False:
  tr_dic[key]=1.0
  tr_word_count[0]=tr_word_count[0]+1.0
 if de_dic.has_key(key)==False:
  de_dic[key]=1.0
  de_word_count[0]=de_word_count[0]+1.0
  
total_word_count[0] = ps_word_count[0]+ng_word_count[0]+tr_word_count[0]+de_word_count[0]

#convert the dictionaries to probability
convert_to_percentage(ps_dic, ps_word_count)
convert_to_percentage(ng_dic, ng_word_count)
convert_to_percentage(tr_dic, tr_word_count)
convert_to_percentage(de_dic, de_word_count)



prior_pro['ps'] = ps_review_count[0]/total_review_count[0]
prior_pro['ng'] = ng_review_count[0]/total_review_count[0]
prior_pro['tr'] = tr_review_count[0]/total_review_count[0]
prior_pro['de'] = de_review_count[0]/total_review_count[0]


output_json_data = {}
output_json_data['ps_dic'] = ps_dic
output_json_data['ng_dic'] = ng_dic
output_json_data['tr_dic'] = tr_dic
output_json_data['de_dic'] = de_dic
output_json_data['prior_pro'] = prior_pro

with open('nbmodel.txt', 'w') as outfile:
    json.dump(output_json_data,outfile, sort_keys = True, indent = 4,ensure_ascii=False)
outfile.close()