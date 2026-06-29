'''Count the frequency of elements'''
nums = [1, 2, 3, 2, 4, 1, 5, 2]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("THE FREQUENCY OF EACH ELEMENT IS: ")
print(freq)