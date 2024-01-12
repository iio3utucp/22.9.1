def binary_search(lst, num):
    low = 0
    high = len(lst) - 1
    search_res = False
    lst = sorted(lst)
    lst = list(map(int, lst))
    if num > lst[-1]:
        print('Введённое число за границей списка')
        return search_res

    while low <= high and not search_res:
        middle = (low + high) // 2
        num_i = lst[middle]
        num_j = lst[middle+1]
        if (num_i < num) and (num_j >= num):
            search_res = True
            print(middle)
            return search_res
        if num_i > num:
            high = middle - 1
        else:
            low = middle + 1

num_lst = input()
num_lst = num_lst.split()
num_lst = list(map(int, num_lst))
val = int(input())
result = binary_search(num_lst, val)
