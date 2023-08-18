import json
import re
invisible_chars = re.compile(r'^\s+$|^\\p{C}+$', re.ASCII)
data = json.load(open('f.txt'))
url_youtube = input("请输入YouTube网址：")
# https://www.youtube.com/watch?v=r6sGWTCMz2k
with open('output.md', 'w') as f:
    for event in data['events']:
        start_time = event['tStartMs']/1000
        start_ms = event['tStartMs']
        start_time = start_ms/1000
        start_min, start_sec = divmod(start_time, 60)

        text = ''
        try:
            for seg in event['segs']:
                text += seg['utf8']

        # 其他代码
        except KeyError:
            pass # 跳过没有segs的事件
        # for seg in event['segs']:
        #     text += seg['utf8']

        text = re.sub(r'([\n])', ' ', text)

        if invisible_chars.match(text) or len(text) == 0:
            # 跳过只包含空白或控制字符的事件
            continue 
        txtline = (f'[{int(start_min):02d}:{start_sec:02.0f}]({url_youtube}#t={start_time}) {text}')
        f.write(txtline + '\n')
