#! /usr/bin/env python
# coding=utf-8

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("original list is: ", a)

temp = a.pop(0)

a.append(temp)

print("final list is: ", a)
