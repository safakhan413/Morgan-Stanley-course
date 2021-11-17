size = ""
type = ""
flavor = ""
state = True

def comparisons(variable, options):
    st = True
    for i in options:
        if variable == i:
            return st
    return False


while state:
    size = input("Choose coffee size: 'Small (S), Medium (M), Large(L):'").upper()
    x = comparisons(size, ['S','M','L'])
    if x:
        state= False
    else:
        print("Please input a valid size")
        continue
state = True
while state:
    type = input("Type of coffee: 'brewed (S), espresso (E), cold brew(C):'").upper()
    x = comparisons(type, ['E','S','C'])
    if x:
        state= False
    else:
        print("Please input a valid type")
        continue
state = True
while state:
    flavor = input("Type of flavoring: 'None (N), All other options(A):'").upper()
    x = comparisons(flavor, ['N','A'])
    if x:
        state= False
    else:
        print("Please input a valid type")
        continue

print(size,type,flavor)