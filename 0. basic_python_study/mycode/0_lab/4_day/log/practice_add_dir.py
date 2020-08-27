from datetime import datetime
# datetime.datetime.now()

import random
from random import random
# from random import random 과 import random의 차이
# random.random() * 100000

import os
# log 디렉토리가 없으면 log 디렉토리를 생성 (폴더를 생성)
if not os.path.isdir('log'):
    os.mkdir('')

b = open('count_log.txt', mode='at', encoding='utf-8')

# for i in range(1, 11):
#     timestamp = str(datetime.now())
#     value = random() * 100000

c = open('count_log.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    timestamp = str(datetime.now())
    value = random() * 100000
    c.write(timestamp, value)