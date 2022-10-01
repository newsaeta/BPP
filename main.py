def exercise_1(list_num):
    data = [max(num) for num in list_num]
    # print(data)
    return data


if __name__ == '__main__':
    integer_list = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
    exercise_1(integer_list)
