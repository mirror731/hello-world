# -*- coding: utf-8 -*-
"""
Takes in a credit card number from a common credit card vendor
and check whether it is a valid number
"""

def checkDigit(n):
    '''checksum of credit card using Luhn Algorithm'''
    luhn = 0
    for x in range(0,15,2):
        if n[x]*2 >= 10:
            digit = n[x]*2 - 10 + 1
            luhn += digit
        else:
            luhn += n[x]*2
    for y in range(1,15,2):
        luhn += n[y]
        
    check = 10 - luhn%10
    
    if check == n[15]:
        return True
    else:
        return False
    
def card_num(n):
    card = []
    temp = list(l for i,l in enumerate(n))
    temp.pop(14)
    temp.pop(9)
    temp.pop(4)
    for x in range(16):
        card.append(int(temp[x]))
    
    return card

def main():
    user_input = input("Enter the credit card no. with'-': ")
    num_list = card_num(user_input)
    if checkDigit(num_list):
        print("Your credit card is valid")
    else:
        print("Sorry. Your credit card is invalid")
        
if __name__ == '__main__':
    main()