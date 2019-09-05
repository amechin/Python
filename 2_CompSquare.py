def comp(array1, array2):
    i = 0
    for i in array1:
        squarenumber = array1[i] * array1[i]
        if squarenumber in array2:
            present = True
        else:
            present = False
    return present