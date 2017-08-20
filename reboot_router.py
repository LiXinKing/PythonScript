#!/usr/bin/python
import requests
import threading
import logging
from sys import argv
from urllib import quote

def securityEncode(a, b, c):
    g = len(a)
    h = len(b)
    k = len(c)
    e = ""

    if g > h:
        f = g
    else:
        f = h

    n = 187
    l = 187
    for p in range(f):
        n = 187
        l = 187
        if p >= g:
            n = ord(b[p: p + 1])
        else:
            if p >= h:
                l = ord(a[p: p + 1])
            else:
                l = ord(a[p: p + 1])
                n = ord(b[p: p + 1])

        m = (l ^ n) % k
        e += c[m: m + 1]

    return e

def getSecurityCode(pass_word, security_1, security_2):
    encode_pwd = securityEncode(pass_word, "RDpbLfCPsJZ7fiv", "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW")
    return quote(securityEncode(security_1, encode_pwd, security_2).decode())

def reboot_router():
    url = "**"
    reboot_url = "**"

    s = requests.session()
    security_data = s.post(url)
    security_lst = security_data.content.split("\r\n")
    security_1 = security_lst[3]
    security_2 = security_lst[4]

    security_code = getSecurityCode("**", security_1, security_2)
    ret = s.post(reboot_url % security_code)
    s.close()
    if ret.content.strip("\r\n") == '00000':
        logging.debug("Reboot Ok")
    else:
        logging.debug("Reboot Error")

def func_timer():
    logging.debug('Timer trigger.')
    reboot_router() # reboot
    global timer
    timer = threading.Timer(7200, func_timer) # two hours timer
    timer.start()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='python_script.log',
                    filemode='w')

timer = threading.Timer(1, func_timer)

if __name__ == "__main__":
    global timer
    if "start" ==  argv[1]:
        timer.start()
        logging.debug("service start")
        print "service start..."
    elif "stop" ==  argv[1]:
        timer.cancel()
        logging.debug("service stop")
        print "service stop..."
    else:
        print "service error cmd..."




