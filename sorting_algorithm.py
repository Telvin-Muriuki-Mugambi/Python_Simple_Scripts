def bubble_sort_algorithm():
    mylist = [42, 50, 19, 5, 31, 20, 6, 21, 7, 16, 3]

    n = len(mylist)
    for i in range(n-1):
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

    print(mylist)

bubble_sort_algorithm()