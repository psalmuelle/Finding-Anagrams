# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


import string


def find_anagrams(subject, anagram):
    """ The functions accepts two parameters, converts them to lower case, creates an empty list, iterate over the two parameters and append the letters into two lists respectively. It sorts them alphabetically,and do a comparison on them """
    
    subject = subject.lower()
    anagram = anagram.lower()

    list_of_subject = []
    list_of_anagram = []

    for letter in subject:
        list_of_subject.append(letter)
    for letter1 in anagram:
        list_of_anagram.append(letter1)
    
    list_of_anagram.sort()
    list_of_subject.sort()

    if list_of_anagram == list_of_subject:
        return True
    else:
        return False


