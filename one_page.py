import requests
import time
import json
import re

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def get_one_page(url1):
    response = requests.get(url1, headers=header)
    return response.content.decode('utf-8')


def get_cursor(response1):
    res = response1[28:-1]
    json1 = json.loads(res)
    cursor = json1["data"]["last"]
    with open('comments.json', 'w',encoding='utf-8') as file:
        for i in range(10):
            comments = json1["data"]["oriCommList"][i]["content"],
            json.dump(comments, file, ensure_ascii=False)
    return cursor

if __name__ == '__main__':
#    cursor = '0'
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294' \
          'commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0'
    source = get_one_page(url)
    time.sleep(3)
    cursor = get_cursor(source)


