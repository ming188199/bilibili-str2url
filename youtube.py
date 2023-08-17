import json
import re

data = json.load(open('f.txt'))
url_youtube = input("请输入YouTube网址：")
#https://www.youtube.com/watch?v=r6sGWTCMz2k
with open('output.md', 'w') as f:
    for event in data['events']:
        start_time = event['tStartMs']/1000
        duration = event['dDurationMs']/1000
        start_ms = event['tStartMs']
        start_time = start_ms/1000
        start_min, start_sec = divmod(start_time, 60)
        
        text = ''
        for seg in event['segs']:
            text += seg['utf8']

        text = re.sub(r'([\n])', ' ', text)
        txtline = (f'[{int(start_min):02d}:{start_sec:02.0f}]({url_youtube}#t={start_time}) {text}')
        f.write(txtline + '\n')
