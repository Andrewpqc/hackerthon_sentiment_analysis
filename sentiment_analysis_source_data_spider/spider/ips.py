import threading
import requests
def fun_timer():
    global ips
    ips = requests.get('http://tvp.daxiangdaili.com/ip/?tid=559677457592481&num=1000&delay=1&category=2&protocol=https').content.decode().split('\r\n')
    global timer
    timer = threading.Timer(1, fun_timer)
    timer.start()

timer = threading.Timer(3, fun_timer)
timer.start()

globals()