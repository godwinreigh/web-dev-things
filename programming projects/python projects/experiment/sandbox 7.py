while True:
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    a = input(" 1,2,3,4,5 ")
    if a == '1':
        for i in range(1):
            list2.append(list1[0])
            print(list2)
    elif a == '2':
        for i in range(1):
            list2.append(list1[1])
            print(list2)
    elif a == '3':
        for i in range(1):
            list2.append(list1[2])
            print(list2)
    elif a == '4':
        for i in range(1):
            list2.append(list1[3])
            print(list2)
    elif a == '5':
        for i in range(1):
            list2.append(list1[4])
            print(list2)
    else:

        exit()