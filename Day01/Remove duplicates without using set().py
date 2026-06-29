'''Remove duplicates without using set()'''
nums = [1, 2, 3, 2, 4, 1, 5]

unique = []
for x in nums:
    if x not in unique:
        unique.append(x)
print("AFTER REMOVING DUPLICATES: ")
print(unique)