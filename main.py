#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
"""
Python 2.7 Katas (Strings and Lists)

You will create a single file for all these exercises 
that should print the requested information to the console.

Several of the katas will use the following sample variables:

    gotCitiesCSV = "King's Landing,Braavos,Volantis,Old Valyria,Free Cities,Qarth,Meereen"

    lotrCitiesList = ["Mordor","Gondor","Rohan","Beleriand","Mirkwood","Dead Marshes","Rhun","Harad"]

    bestThing = "The best thing about a boolean is even if you are wrong you are only off by a bit"

NOTE: follow this pattern in your file for ease of grading
and checking your own work:
print ' 1. ----------------------------'
# code for 1. goes here.
print ' 2. ----------------------------'
# code for 2. goes here

author: bobh "bomazani"
"""


gotCitiesCSV = "King's Landing,Braavos,Volantis,Old Valyria,Free Cities,Qarth,Meereen"
lotrCitiesList = ["Mordor", "Gondor", "Rohan", "Beleriand",
                  "Mirkwood", "Dead Marshes", "Rhun", "Harad"]
bestThing = "The best thing about a boolean is even if you are wrong you are only off by a bit"

print('1. Display a list from the cities in gotCitiesCSV')
answer1 = gotCitiesCSV.split(',')
print(answer1)

print('2. Display a list of words from the sentence in bestThing')
answer2 = bestThing.split()
print(answer2)

print('3. Display a string separated by semi-colons instead of commas from gotCitiesCSV')
answer3 = gotCitiesCSV.split(',')
print(';'.join(answer3))

print('4. Display a CSV (comma-separated) string from the lotrCitiesList')
answer4 = ','.join(lotrCitiesList)
print(answer4)

print('5. Display the first 5 cities in lotrCitiesList')
print(lotrCitiesList[:5])

print('6. Display the last 5 cities in lotrCitiesList')
print(lotrCitiesList[-5:])

print('7. Display the 3rd to 5th city in lotrCitiesList')
print(lotrCitiesList[2:5])

print('8. Using built-in methods, remove "Rohan" from lotrCitiesList')
print(lotrCitiesList.remove('Rohan'))

print('9. Using built-in methods, remove all cities after "Dead Marshes" in lotrCitiesList')
dead_marshes_index = lotrCitiesList.index('Dead Marshes')
del lotrCitiesList[dead_marshes_index + 1:]
print(lotrCitiesList)

print('10. Using built-in methods, add "Rohan" back to lotrCitiesList right after "Gondor"')
gondor_index = lotrCitiesList.index('Gondor')
lotrCitiesList.insert(gondor_index + 1, 'Rohan')
print(lotrCitiesList)


print('11. Using built-in methods, rename "Dead Marshes" to "Deadest Marshes" in lotrCitiesList')
dead_marshes_index = lotrCitiesList.index('Dead Marshes')
del lotrCitiesList[dead_marshes_index]
lotrCitiesList.insert(dead_marshes_index, 'Deadest Marshes')
print(lotrCitiesList)

print('12. Using built-in methods, display the first 14 characters from bestThing')
print(bestThing[:14])

print('13. Using built-in methods, display the last 12 characters from bestThing')
print(bestThing[-12:])

print('14. Using built-in methods, display characters between the 23rd and 38th position of bestThing (i.e., "boolean is even")')
print(bestThing[23:38])

print('15. Find and display the index of "only" in bestThing')
print(bestThing.index('only'))
print(bestThing.find('only'))

print('16. Find and display the index of the last word in bestThing')
best_thing_list = bestThing.split(' ')
last_word = best_thing_list[-1]
print(bestThing.index(last_word))

print('17. Find and display all cities from gotCitiesCSV that use double vowels ("aa","ee", etc.)')
cities = gotCitiesCSV.split(',')
# print(cities)
for city in cities:
    if city.endswith('s'):
        for counter, letter in enumerate(city):
            # print(counter ,letter)
            if city[counter] == city[len(city)-1]:
                break
            elif city[counter] == city[counter + 1]:
                # print(city[counter] + " : " + city[counter + 1])
                print(city)
# Solution
# result = []
# double_vowels = ['aa', 'ee', ...]
# for word in got_cities.split(','):
#     for doubles in double_vowels:
#         if doubles in word:
#             result.append(word)
# result

# Solution 2
# vowel_list = ['aa', 'ee', ...]
# for word in got_cities.split(','):
#     if any (v in word for v in vowel_list):
#         result.append(word)

print('18. Find and display all cities from lotrCitiesList that end with "or"')
for city in lotrCitiesList:
    if city.endswith("or"):
        print(city)
# another option:
# [city for city in lotrCitiesList if city.endswith('or')]
# print(city)

print('19. Find and display all the words in bestThing that start with a "b"')
words_list = bestThing.split(' ')
for word in words_list:
    if word[0] == 'b':
        print(word)
# alternate solution
# print([word for word in bestThing.split() if word[0] == 'b'])

print('20. Display "Yes" or "No" if lotrCitiesList includes "Mirkwood"')
if "Mirkwood" in lotrCitiesList:
    print('Yes')
else:
    print('No')

# alternate solution
# print('yes' if 'Mirkwood' in lotrCitiesList else 'No')

print('21. Display "Yes" or "No" if lotrCitiesList includes "Hollywood"')
if "Hollywood" in lotrCitiesList:
    print('Yes')
else:
    print('No')

print('22. Display the index of "Mirkwood" in lotrCitiesList')
print(lotrCitiesList.index('Mirkwood'))

print('23. Find and display the first city in lotrCitiesList that has more than one word')
for city in lotrCitiesList:
    if " " in city:
        print(city)

print('24. Reverse the order in lotrCitiesList')
print(lotrCitiesList[-1::-1])

print('25. Sort lotrCitiesList alphabetically')
lotrCitiesList.sort()
print(lotrCitiesList)

print('26. Sort lotrCitiesList by the number of characters in each city (i.e., shortest city names go first)')


def sort_by_len(my_list):
    return len(my_list)


lotrCitiesList.sort(key=sort_by_len)
print(lotrCitiesList)

print('27. Using built-in methods, remove the last city from lotrCitiesList')
last_city = lotrCitiesList.pop()
print(lotrCitiesList)

print('28. Using built-in methods, add back the city from lotrCitiesList that was removed in no.27 to the back of the list')
lotrCitiesList.append(last_city)
print(lotrCitiesList)

print('29. Using built-in methods, remove the first city from lotrCitiesList')
first_city = lotrCitiesList[0]
lotrCitiesList.remove(first_city)
print(lotrCitiesList)

print('30. Using built-in methods, add back the city from lotrCitiesList that was removed in no.29 to the front of the list')
lotrCitiesList.insert(0, first_city)
print(lotrCitiesList)
