#!/usr/bin/env python3

#Exercise 1
import sys
fav_thing = str(sys.argv[1])

fav_dict = {'book':'Animal farm', 'Season':'spring', 'Animal':'cat'}
#print(fav_dict['book'])

print(f'Provide a value for {fav_thing}')
y = input()
fav_dict[fav_thing] = y
print(f'The value for {fav_thing} is {fav_dict[fav_thing]}')



#fav_book = 'book'
#print(fav_dict[fav_book])

#fav_dict['organism'] = 'E.coli'
#fav_dict['fav_thing'] = fav_thing
#print(fav_dict['fav_thing'])

#fav_thing = 'book'
#print(fav_dict[fav_thing])

#for thing in fav_dict:
#    print(thing)
#print('Choose one key:')
#x = input()
#print(f'Vlue of {x}: {fav_dict[x]}')

#fav_dict['organism'] = 'M.musculus'
#print(fav_dict['organism'])