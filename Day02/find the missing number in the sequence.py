'''find the missing number in the sequence'''
#using sum formula
def find_missing_sum(arr):
    start = min(arr)
    end = max(arr)
    # Range sum formula: (start + end) * count // 2
    expected_sum = (start + end) * (end - start + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


# Example: print(find_missing_sum([5, 6, 8, 9, 10]))  # 7

# using XOR operation
def find_missing_xor(arr):
    start = min(arr)
    end = max(arr)
    xor_all = 0
    xor_arr = 0

    for i in range(start, end + 1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr

# Example: print(find_missing_xor([5, 6, 8, 9, 10]))  # 7

#Arithmetic progression
def find_missing_ap(arr):
    n = len(arr) + 1
    d = (arr[-1] - arr[0]) // len(arr) #any number can be missing so obtained a total diff divided by total diff in number of elements

    for i in range(len(arr) - 1):  #loop runs unti third last elemet to prevent index error
        if arr[i + 1] - arr[i] != d:
            return arr[i] + d

    return None

# Example: print(find_missing_ap(arr))  # 8

#Geometric Progression
def find_missing_gp(arr):
    n = len(arr) + 1
    #first term
    a = arr[0]
    #common ratio usingnth root of last term divided by first term
    r = round((arr[-1] / arr[0]) ** (1 / len(arr)))  #round is used because any number can be missing so we use round to get the common ratio

    for i in range(len(arr) - 1):  #loop runs unti third last elemet to prevent index error
        if arr[i + 1] != arr[i] * r:  #if the next element is not equal to the current element multiplied by the common ratio
            return arr[i] * r  #the missing number is the current element multiplied by the common ratio

    return None  #if no missing number is found

# Example: print(find_missing_gp(arr))  # 54

def main():
    choice=int(input("ENTER 1 for sum formula\nENTER 2 for XOR operation\nENTER 3 for Arithmetic progression\nENTER 4 for Geometric Progression\n ENTER 5 to exit\n"))
    if choice==1:
        arr=list(map(int,input("Enter the array elements separated by spaces: ").split()))
        print(find_missing_sum(arr))
    elif choice==2:
        arr=list(map(int,input("Enter the array elements separated by spaces: ").split()))
        print(find_missing_xor(arr))
    elif choice==3:
        arr=list(map(int,input("Enter the array elements separated by spaces: ").split()))
        print(find_missing_ap(arr))
    elif choice==4:
        arr=list(map(int,input("Enter the array elements separated by spaces: ").split()))
        print(find_missing_gp(arr))
    elif choice==5:
        exit()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
