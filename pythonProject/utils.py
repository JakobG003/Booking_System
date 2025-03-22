def find_max(x):
    max_number = x[0]
    for number in x:
        if number > max_number:
            max_number = number
    return max_number
