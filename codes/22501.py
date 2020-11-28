#! /usr/bin/env python3
# coding=utf-8

import urllib.request

def go(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print("%.2f%%" % per)

url = "http://www.sinaimg.cn/nw690/8e4023f8gw1f34gs20bsij20qo0zkthw.jpg"
local = "/home/jeffery/Pictures/g.jpg"
urllib.request.urlrretrieve(url, local, go)
