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
    cursor = json1["data"]["last"]
    get_one_page_comments(json1)
    return cursor

def get_one_episode_comments(response1):
    res = response1[28:-1]
    json1 = json.loads(res)
    total_comments = json1["data"]["oritotal"]
    return total_comments


def get_one_page_comments(json1):
    num = json1["data"]["orirenum"]
    with open('comments.json', 'a+', encoding='utf-8') as file:
        for i in range(int(num)):
            comments = json1["data"]["oriCommList"][i]["content"],
            json.dump(comments, file, ensure_ascii=False)


if __name__ == '__main__':
    cursor = '0'
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294' \
          'commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+cursor
    source = get_one_page(url)
    time.sleep(3)
    cursor = get_cursor(source)
    total_comments = get_one_episode_comments(source)
    for i in range(int(int(total_comments)/10+1)):
        url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294' \
          'commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+cursor
        source = get_one_page(url)
        print(url)
        time.sleep(5)
        cursor = get_cursor(source)







