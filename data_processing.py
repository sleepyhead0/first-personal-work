import jieba
import jieba.analyse
import json

dic = {}
stop_keyword=[line.strip() for line in open('stop.txt',encoding='utf-8').readlines()]
with open(r"all_comments.json","r",encoding='utf-8') as file:
    for jsonstr in file.readlines():
        seg_list = jieba.analyse.extract_tags(jsonstr, topK=10)  #关键词过滤
        for seg in seg_list:
             if seg in dic:
                 dic[seg] += 1
             else:
                 dic[seg] = 1

for key in list(dic.keys()):
    if key in stop_keyword or dic[key] <= 5:
        del dic[key] #出现次数小于等于5的词没有较大的参考意义，故删除
        continue


commentlist = []
for key in dic.keys():
    comment = {}
    comment["name"] = key
    comment["value"] = dic[key] #将单个词和出现次数组成键值对
    commentlist.append(comment)

with open(r"All_processed_data.json","a+",encoding='utf-8') as file:
    for comment in commentlist:
        file.write(json.dumps(comment, ensure_ascii=False)+'\n')   #处理后的词频写入json文件