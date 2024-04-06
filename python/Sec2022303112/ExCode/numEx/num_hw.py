#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from math import *

# 题目九：两地之间距离计算

# 计算两点p1, p2之间的距离
# p1：（纬度、经度）
# p2: （纬度、经度）
def sphere_distance(p1, p2):
    lat1, lon1, lat2, lon2 = p1[0], p1[1], p2[0], p2[1]
    if lat1 < 0 or lat1 > 90 or lat2 < 0 or lat2 > 90 :
        return "Parameter Error."
    if lon1 < 0 or lon1 > 180 or lon2 < 0 or lon2 > 180:
        return "Parameter Error."
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    d = 2 * asin(sqrt(a)) * 6371
    return d

# 题目十：计算Fibonacci 序列的值
# Fibonacci是1，1, 2，3，5, 8，13.....
# n1 = 1, n2 =2, n3 = n1+n2, n4 = n3+n2
def fibonacci_recursion(number):
    if number < 1 :
        return "Parameter Error."
    if number == 1:
        return 1
    if number == 2:
        return 1
    else :
        return fibonacci_recursion(number-1) + fibonacci_recursion(number-2)

def fibonacci_loop(number):
    if number < 1 :
        return "Parameter Error."
    if number == 1:
        return 1
    if number == 2:
        return 1
    n1 = 1
    n2 = 1
    n = 0
    i = 3
    while i <= number:
        n = n1 + n2
        n1 = n2
        n2 = n
        i += 1
    return n




# 题目一：水仙花数
def narcissistic_number():
    i = 100
    ans = []
    while i < 1000:
        a = i % 10
        b = int(i / 10 % 10)
        c = int(i / 100)
        if a**3 + b**3 + c**3 == i:
            ans.append(i)
        i += 1
    return ans




# 题目二：完美数
def perfect_number(limit=1000):
    if limit < 1:
        return "Parameter Error."
    i = 2
    ans = []
    cnt = 0
    while i <= limit:
        j = 2
        while j**2 <= i:
            if i % j == 0:
                if j**2 == i:
                    cnt += j
                else:
                    cnt += (j + int(i/j))
            j += 1
        if i == (cnt + 1):
            ans.append(i)
        i += 1
        cnt = 0
    return ans



# 题目三：百钱百鸡
def buy_chicken():
    a = 0
    b = 0
    ans = []
    while a <= 20:
        b = 0
        while b <= int((100 - 5 * a)/3):
            rest = 100 - 5 * a - 3 * b
            if (a + b + 3 * rest) == 100:
                ans.append([a, b, rest*3])
            b += 1
        a += 1
    return ans


#题目四
# 最大公约数
def gcd(x, y):
    if x <= 0 or y <= 0:
        return "Parameter Error."
    m = x
    n = y
    if m < n:
        tmp = m
        m = n
        n = tmp

    r = m % n
    while r:
        m = n
        n = r
        r = m % n
    return n




# 最小公倍数
def lcm(x, y):
    if x <= 0 or y <= 0 :
        return "Parameter Error."
    t = gcd(x, y)
    return int(x * y / t)



# 题目五：回文数
def is_palindrome_number(num):
    a = str(num)
    b = a [::-1]
    if a == b:
        return True
    else :
        return False

# 题目六：素数
def is_prime_num(num):
    if type(num) != int  or num <= 0 :
        return "Parameter Error."
    else:
        if num == 2:
            return True
        i = 2
        while i**2 <= num:
            if num % i == 0:
                return False
            i += 1
        return True



# 题目七：约瑟夫环
def jose_prob(n, m):
    if n >= m or n <=0 or m <=0 or type(n) != int or type(m) != int :
        return "Parameter Error."
    l = []
    for i in range(m):
        l.append(1)
    pointer = 8 % m # 9 % m -1 = 8 % m
    num = m
    while num > n:
        l[pointer] = 0
        num -= 1
        tmp = 0
        while tmp < 9 :
            pointer = (pointer + 1) % m
            if l[pointer] :
                tmp += 1

    return l
# 题目八：万年历
def calendar(year, month, day):
    whole_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12:
        return "Parameter Error."
    if month in [1, 3, 5, 7, 8, 10, 12] and day >31 :
        return "Parameter Error."
    elif month in [4, 6, 9, 11] and day > 30:
        return "Parameter Error."
    if month == 2 :
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            if day > 29:
                return "Parameter Error."
        else :
            if day > 28 :
                return "Parameter Error."
            whole_month[1] = 28
    date = day
    i = 0
    while i < (month -1):
        date += whole_month[i]
        i += 1

    return date





if __name__ == '__main__':
    calendar(2012,7,12)
