# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:27:23 2019

Topic: Convert interger value from Decimal to any Base
"""

from pythonds.basic import Stack
def baseConvert(decimalVal, base):
    stack = Stack()
    digit = '0123456789ABCDEF'
    while decimalVal > 0:
        remainVal = decimalVal % base
        stack.push(remainVal)
        decimalVal = decimalVal // base
    
    binstring = ""
    while not stack.isEmpty():
        binstring = binstring + str(digit[stack.pop()])
        
    return binstring

print(baseConvert(233,16))
