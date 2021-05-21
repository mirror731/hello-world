# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:35:56 2021

check whether a number is a huppay number
"""

def numSquareSum(n):
    squareSum = 0
    n = str(n)
    l = list(n)
    l = list(map(int,l))
    for i in l:
        squareSum += i**2
    return squareSum

def main():
    n = int(input("Check whether is happy number or not: "))
    origin = n
    sumlist = []
    while True:
        if numSquareSum(n) not in sumlist:
            if numSquareSum(n) == 1:
                print(f"{origin} is a Happy number")
                break
            else:
                sumlist.append(numSquareSum(n))
                n = numSquareSum(n)
        else:
            print(f"{origin} is not a Happy number")
            break
        
if __name__ == '__main__':
    main()