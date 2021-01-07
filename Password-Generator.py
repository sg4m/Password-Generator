#!/bin/python3
import random

chars ='abcdefghjklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890!"#$%&/()=¿?'

print ('Hey!')
print ('This Generator only works with numbers :)')
print ('made by: s_g')

print ('')

print ('Hola!')
print ('Este generador funciona solo con números :)')
print ('Hecho por: s_g')

print ('')

length = input('Password length?:')
lenght = int(length)

quantity = input('How many?:')
quantity = int(quantity)

print ('Your passwords:')

for p in range(quantity):
  password =''
  for c in range(lenght):
    password += random.choice(chars)
  print (password)
  
  
  
  
  