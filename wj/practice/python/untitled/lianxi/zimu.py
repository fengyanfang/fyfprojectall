a = '12hhj5jjHhfdfffffffagajkh603bjfdk44nnn3r'
def test(x):
    num = []
    dict = {}
    for one in x:

        if one.isdigit():
            num.append(one)
        else:
            dict[one] = x.count(one)
    print dict
    print num


test(a)