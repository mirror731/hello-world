# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:27:11 2021

enter a cost and either a country or state tax. 
returns the tax plus the total cost with tax.
"""

tax_rate = {"Country":{'JP':.1, 'KR':.1, 'SG':.07, 'TW':.05, 'UK':.2, 'AU':.1, 'CA':.05, 'IT':.22, 'ES':.21, 'FR':.2, 'DE':.19}, 
            "State":{'CA':.0848, 'AZ':.0825, 'TX':.0817, 'FL':.0666, 'NY':.0849, 'PA':.0634, 'GA':.0701}}

def main():
    user_input = input("Looking tax of (1) country or (2) state: ")
    if user_input == "1":
        choice = "Country"
        rate = input("Enter the alpha-2 code of the country\n eg Japan=JP, Canada=CA: ")
    elif user_input == "2":
        choice = "State"
        rate = input("Enter the alpha-2 code of the state\n eg CA,TX,AZ: ")

    cost = float(input("Enter the cost: "))
    total = cost * (1 + tax_rate[choice][rate])
    print(f"Total cost of ${cost} with tax rate {tax_rate[choice][rate]*100}% is ${total:.2f}")
    
if __name__ == '__main__':
    main()