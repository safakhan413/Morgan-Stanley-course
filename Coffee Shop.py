size = ""
type = ""
state = True

def comparisons(variable, options):
    st = True
    for i in options:
        # print(i)
        if variable == i:
            return st
    return False


while state:
    size = input("Choose coffee size: 'Small (S), Medium (M), Large(L):'")
    x = comparisons(size, ['S','M','L'])
    if x:
        state= False
    # print('hey')
    # print(x)
    # if size == 'S' or size == 'M' or size == 'L':
    #     state = "False"
        # type = input("Type of coffee: 'brewed (S), espresso (E), cold brew(C):'")
        # # if type == 'E' or type == 'S' or type == 'C':
        # #     print(type)
        # #  else:
        # #     print("Please input a valid size")
        # #     continue
        # print(size)
    else:
        print("Please input a valid size")
        continue
