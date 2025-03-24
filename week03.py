def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return(a_list)

# def move_zeros(l):
#     zero_idx = 0
#     for i in range(len(l)):
#         n = l[i]
#         if n != 0:
#             l[zero_idx] = n
#             if zero_idx != i:
#                 l[i] = 0
#             zero_idx = zero_idx + 1
#     return l

a_list = [8, 0, 3, 0, 12]
move_zeros(a_list)
print(a_list)

# l = [11, 9, -77, 8]
#  for i, v in enumerate(l):
#      print(i, v)
#
# # l = [11, 9, -77, 8]
#  # for i in range(len(l)):
#  #     print(i, l[i])