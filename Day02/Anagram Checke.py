'''Anagram Checker: An anagram checker is a tool or algorithm that determines whether two words or phrases are anagrams of each other. Two strings are anagrams if they contain exactly the same letters with the same frequencies, but arranged in a different order.'''

s1=str(input('Enter the string1:'))
s2=str(input('Enter the string2:'))

s1=s1.lower()                  # convert to lowercase
s2=s2.lower()                  # convert to lowercase

s1=sorted(s1)                  # sort the string
s2=sorted(s2)                  # sort the string

if(s1==s2):
    print('Is an Anagram')      # check if the sorted strings are equal
    freq1 = {}
    freq2 = {}
    for num in s1:                         # Count how many times each letter appears and compare the counts.
        if num in freq1:
            freq1[num] += 1
        else:
            freq1[num] = 1
            print("THE FREQUENCY OF EACH ELEMENT IS: ")
            print(freq1)

    for num in s2:
        if num in freq2:
            freq2[num] += 1
        else:
            freq2[num] = 1
            print("THE FREQUENCY OF EACH ELEMENT IS: ")
            print(freq2)

    if (freq1==freq2):
        print("Is an Anagram")
    else:
        print("Is not an Anagram")    

else:
    print('Is not an Anagram')    # check if the sorted strings are not equal