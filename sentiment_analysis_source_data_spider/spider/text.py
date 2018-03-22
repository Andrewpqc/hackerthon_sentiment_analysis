# with open('//home/lenovo/桌面/PythonEx/Test/Test/ipport.txt','r') as f:
#     ips=f.readlines()
#
#
# import random
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print(random.choice(ips))
# print('dssssssssssss')
# print('dssssssssssss')

import requests
a=requests.get('http://tvp.daxiangdaili.com/ip/?tid=559677457592481&num=1000&delay=1&category=2&protocol=https')
print(a)
c=a.content.decode().split('\r\n')
for i in c:
    print(i)