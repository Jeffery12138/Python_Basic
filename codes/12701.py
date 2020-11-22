#! /usr/bin/env python
# coding=utf-8

f = open("../第二章 语句和文件/file/you.md")

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()
