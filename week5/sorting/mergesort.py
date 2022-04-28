def mergeSort(nlist):
    print("Splitting ",nlist)
    lengthList = len(nlist)
    if lengthList == 1:
        return nlist
    if lengthList > 1:

        mid = lengthList // 2

        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
    print("Merging ",nlist)
    return merge(nlist, lefthalf, righthalf)
    

# insert your code to complete the mergeSort function
    
def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

list = [ 55, 31, 26, 20, 63, 7, 51, 74, 81, 40 ]

print(list)
mergeSort(list)
print("Sorted")
print(list)