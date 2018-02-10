#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:46:59 2018

@author: mural.kummitha
"""

# assignment of variables

counter = 100
miles = 1000.00
name = "John"
#print counter
print(counter)
print(miles)
print(name)


# multiple assignment

a = b = c = 1 # assignns same memory location
print(a, b, c, sep='-')
a = 3
print(a, b, c, sep='-')

a, b, c = 2, 3, 4
print(a, b, c, sep='-')

# strings

string = "Hellow world"

print(string)
print(string[2:])
print(string[2:4])
print(string*2)
print(string + " Test ")

# lists
listitems = ['abcd', 123, 'helow']
tinylist = ['boss', 'bob']

print(listitems)
print(listitems[2:3])
print(listitems + tinylist)
print(listitems*2)


# tupule

tuples = ('abcd', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tuples)
print(tuples*2)
print(tuples[2])
print(tuples + tinytuple)

# dictionaries (hashes)
dictonary = {'one': 'one-two', 2: '3-4'}
print(dictonary)
print(dictonary.keys())
print(dictonary.values())


# data type conversions

print(int('2', 10))
print(int(12.03))

inum = complex(3, 2)
print(inum)

inum2 = complex(4, 6)
print(inum+inum2)
print(inum*inum2)

print(tuple('1'))
chr(1)

oct(10)


# python loops
var = 100
if (var == 100) : print('yes truth single line stmt')

if (var == 100):
  print ('yes it"s multi line stmt')
else:
  print ('no value is not 100: something is worng')

# loops

i = 0
while (i<10):
  i += 1
  print(i)
  
print ('----------')
i = 10
while i < 12:
  print (i)
  i += 1
else:
  print ('end of while stmt;')
  
for letter in 'Python':
  print(letter)
  
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:
  print(fruit)

for i in range(len(fruits)):
  print('current fruit is: ', fruits[i])
  

for num in range(10, 20):
  for i in range(2, num):
    if (num % i == 0):
      j = num / i
      print(num, " equals ", i,  " * ", j)
      break;
    else:
      print(num, "is a prime number")

for letter in 'Python':
  if (letter == 't'):
    print('breakinig')
    break;
  print(letter)
        
for letter in 'Python':
  if (letter == 't'):
    print('continuing')
    continue;
  print(letter)

for letter in 'Python':
  if (letter == 't'):
    print('pass')
    pass;
  print(letter)