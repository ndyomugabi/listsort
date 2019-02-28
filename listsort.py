def list_sort(mylist):

    characters =[]
    odd = []
    even = []
    mydict = dict()
    if not isinstance(mylist, list):
        return 'Invalid Input'

    if not mylist:
        mydict['evens'] = even
        mydict['odds'] = odd
        mydict['chars'] = characters
        return mydict

    for s in mylist:

        if isinstance(s, int):
            if s % 2 == 0:
                even.append(s)

            else:
                odd.append(s)

        elif isinstance(s, str):
            characters.append(s)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(characters)
    return mydict


print(list_sort([1, 7, 4, 5, 'x', 'y']))