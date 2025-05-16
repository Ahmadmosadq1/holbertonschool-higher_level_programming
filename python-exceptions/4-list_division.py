#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
            # Dividing each index of list_1 with its respective index in list 2
            result = my_list_1[index] / my_list_2[index]
        # exception for wrong type error
        except TypeError:
            print("wrong type")
            result = 0
        # exception for zero division error
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        # exception for out of range erorr
        except IndexError:
            print("out of range")
            result = 0
        finally:
            # Apeeding the result in the new list
            new_list.append(result)
    return new_list
