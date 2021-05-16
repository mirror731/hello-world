# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:29:05 2021

calculate the salary tax in Hongkong
"""

def s_tax(n):
    if n <= 50000:
        tax = n*0.02
    elif n <= 100000:
        tax = 1000 + (n - 50000)*0.06
    elif n <= 150000:
        tax = 4000 + (n - 100000)*0.1
    elif n <= 200000:
        tax = 9000 + (n - 150000)*0.14
    elif n > 200000:
        tax = 16000 + (n - 200000)*0.17
    return tax

def allowance():
    basic = 132000
    child = int(input("How many child do you carry(if no, enter '0'): "))
    c_allowance = child*120000
    elderly = int(input("How many dependent parent/grandparent aged over 60 do you carry(if no, enter '0'): "))
    e_allowance = elderly*100000
    return basic + c_allowance + e_allowance
    
def main():
    salary = float(input("Enter your annual salary: "))
    total_allowance = allowance()
    std_tax = salary * 0.15
    salary -= total_allowance
    tax = s_tax(salary)
    if tax > std_tax:
        tax = std_tax 
    
    print(f"Your salary tax is ${tax}")