# Merge sort

def merge_sort(liste):
    if len(liste) <= 1:
        return liste
    if len(liste) == 2:
        if liste[0] > liste[1]:
            liste[0],liste[1] = liste[1], liste[0]
        return liste
    mid = len(liste)//2
    r1, r2 = merge_sort(liste[:mid]), merge_sort(liste[mid:])
    return merge(r1,r2)

def merge(liste1, liste2):
    i1, i2 = 0,0
    merged_list = []
    while i1 < len(liste1) and i2 < len(liste2):
        if liste1[i1] <= liste2[i2]:
            merged_list.append(liste1[i1])
            i1 += 1
        else:
            merged_list.append(liste2[i2])
            i2 += 1
    while i1 < len(liste1):
        merged_list.append(liste1[i1])
        i1 += 1
    while i2 < len(liste2):
        merged_list.append(liste2[i2])
        i2 += 1
    return merged_list

liste2 = [54,36]
print(merge_sort(liste2))
arr = [23,54,35,11,53,67,45,60,34,56]
print(merge_sort(arr))