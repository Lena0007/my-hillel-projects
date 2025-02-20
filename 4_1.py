def move_zeros(list):
    non_zeros = []
    zeros = []

    for num in  list:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    return non_zeros + zeros

print(move_zeros([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))
