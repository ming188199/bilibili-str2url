import requests
def download_str(url):
    # 发送GET请求获取文件内容
    response = requests.get(url)

    # 写入文件
    with open("str.json", "wb") as f:
        f.write(response.content)

url_str = input('字幕网址') # 可临时下载
# just for test
# url_str = 'https://aisubtitle.hdslb.com/bfs/ai_subtitle/prod/20624185337534032221caeb77d0d7ce61f5dbf8f14d4de5?auth_key=1690605908-29d09c3e41514887882d035c0ac7cf38-0-524c9b64862d4efacc5d0ed207f8fa55'
download_str(url_str)


import json
with open('str.json') as f:
  data = json.load(f)
body = data["body"]
url_bilibili = input("Bilibili视频网址")
with open('output.md', 'w') as f:
    for item in body:
        timestamp = item["from"]
        content = item["content"]
        minute = int(timestamp / 60)
        second = int(timestamp % 60)
        link = f'[{minute}:{second:02d}]({url_bilibili}#t={timestamp}){{>{content}}}'
        f.write(link + '\n')
        # print(link)
