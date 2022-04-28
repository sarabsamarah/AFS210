list1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

def binarySearch(list, num):
    first = 0
    last = len(list)-1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if list[mid] == num:
            found = True
        else:
            if num < list[mid]:
                last = mid-1
            else: 
                first = mid+1
    return found
    

print(binarySearch(list1, 31))
print(binarySearch(list1, 77))
print(binarySearch(list2, "Delta"))