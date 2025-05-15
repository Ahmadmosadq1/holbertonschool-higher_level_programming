def search_replace(my_list, search, replace):
    # Slicing the whole matrix to keep the orginal matrix
    copy_list = my_list[:]
    # looping through the copy matrix
    # Finding the element of search and replace it
    for index in range(len(copy_list)):
        if copy_list[index] == search:
            copy_list[index] = replace
    return copy_list
