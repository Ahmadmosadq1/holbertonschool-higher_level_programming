def max_integer(list=[]):
    if len(list) == 0:
        return None
    result = list[0]
    for i in list[1:]:
        if i > result:
            result = i
    return result
