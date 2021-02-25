import requests
import time
import json

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def get_one_page(url1):
    response = requests.get(url1, headers=header)
    return response.content.decode('utf-8')

def get_cursor(response1):
    res = response1[28:-1]
    json1 = json.loads(res)
    cursor = json1["data"]["last"] #下一页评论内容地址的标志
    get_one_page_comments(json1)
    return cursor

def get_one_episode_comments(response1):
    res = response1[28:-1]
    json1 = json.loads(res)
    total_comments = json1["data"]["oritotal"] #确定每集的评论总数
    return total_comments

def get_one_page_comments(json1):
    num = json1["data"]["oriretnum"] #确定每页评论数
    with open('comments.json', 'a+', encoding='utf-8') as file: # 每页评论写入json文件
        for i in range(int(num)):
            comments = str(json1["data"]["oriCommList"][i]["content"]).replace("(","").replace(")","")
            file.write(json.dumps(comments, ensure_ascii=False)+'\n')

if __name__ == '__main__':
    ID = ['5963120294','5963137527','5963276398','5963339045','5963339045','5974620716','5979269414',
          '5979342237','5979747069','5979699081','5980549863','5980559005','5990521528','5984189515',
          '5984155079','5984165842','5995355954','5995862740','5991853633','5991863028']  #《在一起》20集集评论不同的地址
    for id in ID: # 循环得到20集全部评论
        url = 'https://coral.qq.com/article/'+id+'/comment/v2?callback=_article'+id\
              +'commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0' # 构造每一集评论的初始地址
        source = get_one_page(url)
        time.sleep(3)
        cursor = get_cursor(source)
        total_comments = get_one_episode_comments(source)
        for i in range(int(int(total_comments)/10+1)): # 循环得到每集全评论
            url = 'https://coral.qq.com/article/'+id+'/comment/v2?callback=_article'+id\
              +'commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' +cursor  #构造每集的评论地址的后续地址
            source = get_one_page(url)
            time.sleep(5)
            cursor = get_cursor(source)







