# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:58:44 2021

@author: User
convert unit in different parameter
"""

def temp(unit1,unit2,x):
    if unit1 == "Celsius" and unit2 == "Fahrenheit":
        ans = x*(9/5)+32
    elif unit2 == "Celsius" and unit1 == "Fahrenheit":
        ans = (x-32)*(5/9)
    elif unit1 == "Celsius" and unit2 == "Kelvin":
        ans = x+273.15
    elif unit2 == "Celsius" and unit1 == "Kelvin":
        ans = x-273.15
    elif unit1 == "Kelvin" and unit2 == "Fahrenheit":
        ans = x*(9/5)-459.67
    elif unit2 == "Kelvin" and unit1 == "Fahrenheit":
        ans = (x+459.67)*5/9
    print(f"{x} in {unit1} is equal to {ans} in {unit2}")
    
def length(unit1,unit2,x):
    if unit1 == "cm" and unit2 == "m":
        ans = x/100
    elif unit2 == "cm" and unit1 == "m":
        ans = x*100
    elif unit1 == "cm" and unit2 == "km":
        ans = x/100000
    elif unit2 == "cm" and unit1 == "km":
        ans = x*100000
    elif unit1 == "m" and unit2 == "km":
        ans = x/1000
    elif unit2 == "m" and unit1 == "km":
        ans = x*1000
    elif unit1 == "cm" and unit2 == "in":
        ans = x/2.54
    elif unit2 == "cm" and unit1 == "in":
        ans = x*2.54
    elif unit1 == "m" and unit2 == "in":
        ans = x/2.54*100
    elif unit2 == "m" and unit1 == "in":
        ans = x*2.54/100
    elif unit1 == "km" and unit2 == "in":
        ans = x/2.54*100000
    elif unit2 == "km" and unit1 == "in":
        ans = x*2.54/100000
    print(f"{x} {unit1} is equal to {ans:.4f} {unit2}")
    
def weight(unit1,unit2,x):
    if unit1 == "g" and unit2 == "kg":
        ans = x/1000
    elif unit2 == "g" and unit1 == "kg":
        ans = x*1000
    elif unit1 == "kg" and unit2 == "lb":
        ans = x*2.205
    elif unit2 == "kg" and unit1 == "lb":
        ans = x/2.205
    elif unit1 == "g" and unit2 == "lb":
        ans = x/1000*2.205
    elif unit2 == "g" and unit1 == "lb":
        ans = x*1000/2.205
    elif unit1 == "oz" and unit2 == "lb":
        ans = x/16
    elif unit2 == "oz" and unit1 == "lb":
        ans = x*16
    elif unit1 == "kg" and unit2 == "oz":
        ans = x*16*2.205
    elif unit2 == "kg" and unit1 == "oz":
        ans = x/16/2.205
    elif unit1 == "g" and unit2 == "oz":
        ans = x*16*2.205/1000
    elif unit2 == "g" and unit1 == "oz":
        ans = x/16/2.205*1000
    print(f"{x} {unit1} is equal to {ans:.4f} {unit2}")
    
import requests
import json

class CurrencyConverter():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]

    def cur_convert(self,from_cur,to_cur,amount):
        initial_amount = amount
        if from_cur != "USD": # convert to USD first
            amount = amount / self.currencies[from_cur]
            
        amount = round(amount * self.currencies[to_cur], 4) # limit to 4 d.p.
        
        print(f"{initial_amount} {from_cur} is equal to {amount} {to_cur}")



def main():
    print("You can convert the following parameters")
    print("Temperature: Celsius, Fahrenheit, Kelvin")
    print("Length: cm, m, km, in")
    print("Weight: g, kg, lb, oz")
    print("Currency")
     
    unit1 = input("Enter the parameter you want to convert from: ")
    unit2 = input("Enter the parameter you want to convert to: ")
    x = float(input("Enter the value: "))
    
    if unit1 and unit2 in ["cm","m","km","in"]:
        length(unit1,unit2,x)
    elif unit1 and unit2 in ["g","kg","lb","oz"]:
        weight(unit1,unit2,x)
    elif unit1 and unit2 in ["Celsius, Fahrenheit, Kelvin"]:
        temp(unit1,unit2,x)
    else:
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        converter = CurrencyConverter(url)
        converter.cur_convert(unit1,unit2,x)

if __name__ == '__main__':
    main()

