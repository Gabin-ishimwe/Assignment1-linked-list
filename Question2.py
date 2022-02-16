# we are going to implement an algorithm the calculates
# the sum of k largest numbers in the list

def sum(arr, k):
    non_duplicate = set(arr)
    list_back = list(non_duplicate)
    list_back.sort(reverse=True)
    print(list_back)
    sum_results = 0
    for i in range(k):
        sum_results += list_back[i]
    print(sum_results)


sum([1, 6, 7, 2, 3, 3, 20, 18, 15, 3], 3)
