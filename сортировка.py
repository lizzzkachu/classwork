# list = [1, 4, 2, 5, 3, 6, 7, 2, 7]


# def bubble_sort(list):
#     for i in range(len(list)):
#         flag = False
#         for j in range(len(list) - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#                 flag = True
#         if not flag:
#             break
#
#
# if __name__ == '__main__':
#     bubble_sort(list)
#     print(list)


# def insertion_sort(list):
#     counter = 0
#     for i in range(len(list)):
#         for j in range(i, 0, -1):
#             if list[j] < list[j - 1]:
#                 list[j], list[j - 1] = list[j - 1], list[j]
#             else:
#                 break
#             counter += 1
#
#
# if __name__ == '__main__':
#     print(list)
#     insertion_sort(list)
#     print(list)


# def shaker_sort(list):
#     l_i = 0
#     r_i = len(list) - 1
#     for i in range (int(len(list)/2)):
#         while(l_i,r_i):
#             flag = True
#             for j in range(l_i, r_i):
#                 if list[j] > list[j + 1]:
#                     list[j], list[j + 1] = list[j + 1], list[j]
#                     flag = False
#             if (flag): break
#             print(list)
#             r_i -= 1
#             flag = True
#             for j in range(l_i, r_i, -1):
#                 if list[j] > list[j - 1]:
#                     list[j], list[j - 1] = list[j - 1], list[j]
#                     flag = False
#             if (flag): break
#             print(list)
#             l_i+=1
#
# if __name__ == '__main__':
#     shaker_sort(list)
#     print(list)


list = [2, 1, 3, 1, 1, 7, 6, 1, 3, 7, 2, 2]


def maximum(list):
    max = list[0]
    for i in list:
        if i > max: max = i
    return max


def counting_sort(list):
    max = maximum(list)
    list2 = [0 for i in range(max + 1)]
    result_list = []
    for i in list:
        list2[i] += 1
    for i in range(len(list2)):
        while (i > 0):
            result_list.append(i)
            list2[i] -= 1
    return result_list


if __name__ == '__main__':
    list = counting_sort(list)
    print(list)
