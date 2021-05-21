# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:31:00 2021

Showing the first 8 happy numbers
"""

def numSquareSum(n):
    squareSum = 0
    n = str(n)
    l = list(n)
    l = list(map(int,l))
    for i in l:
        squareSum += i**2
    return squareSum

def isHappy(n):
    sumlist = []
    origin = n
    while True:
        if numSquareSum(n) not in sumlist:
            if numSquareSum(n) == 1:
                return origin
                break
            else:
                sumlist.append(numSquareSum(n))
                n = numSquareSum(n)
        else:
            break

def main():
    print("A happy number is defined by the following process.\nStarting with any positive integer,\nreplace the number by the sum of the squares of its digits,\nand repeat the process until the number equals 1 (where it will stay),\nor it loops endlessly in a cycle which does not include 1.")
    print("For example 440 is a happy number")
    start = input("Do you want to know first 8 happy numbers? Y or N: ")
    if start == "Y":
        happynums = set()
        for n in range(1000):
            if len(happynums) < 9:
                happynums.add(isHappy(n))   
        happynums.remove(None)
        print("The first 8 happy nunmbers are:")
        print(happynums)
    else:
        print("See you")
    
if __name__ == '__main__':
    main()