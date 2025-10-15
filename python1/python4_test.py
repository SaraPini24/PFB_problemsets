#!/usr/bin/env python3

taxa_string = "sapiens : erectus : neanderthalensis"
print(taxa_string)

#Split taxa_string into a list called taxa_list. Use " : " as your separator.
taxa_list = taxa_string.split(' : ')
print(taxa_list)

print(taxa_list[1])

print(type(taxa_string))
print(type(taxa_list))

#Sort the list alphabetically and print 
print(sorted(taxa_list))

# Sort the list by length of each string and print.
print(sorted(taxa_list, key=len))