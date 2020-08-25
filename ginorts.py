def compare(a,b):
    # is a < b?
    if a.isupper() and b.isupper():
        return a < b
    if a.isupper() and b.islower():
        return False
    if a.islower() and b.isupper():
        return True
    if a.islower() and b.islower():
        return a < b
    if a.isnumeric() and not b.isnumeric():
        return False
    if b.isnumeric() and not a.isnumeric():
        return True
    if a.isnumeric() and b.isnumeric():
        x = int(a)
        y = int(b)
        if x%2 == 0 and y%2 == 0:
            return x < y
        if x%2 == 1 and y%2 == 1:
            return x < y
        if x%2 == 1 and y%2 == 0:
            return True
        if x%2 == 0 and y%2 == 1:
            return False
    print("here", a, b)
    return a< b

def bubbleSort(arr): 
    l = len(arr) 
    for i in range(0,l-1): 
        for j in range(0, l-i-1): 
            if compare(arr[j+1],arr[j]) : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

if __name__ == '__main__':
    str1 = input()
    ls = [char for char in str1]
    bubbleSort(ls)
    print("".join(ls))
