list_1 = [0, 1, 7, 2, 4, 8]

if len(list_1) == 0:
    result = 0

else:
    result = 0
    for i in range(0, len(list_1), 2):
        result += list_1[i]
    result *= list_1[-1]
print(result)
