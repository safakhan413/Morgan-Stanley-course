size = ""

while True:
    size = input("Choose coffee size: 'Small (S), Medium (M), Large(L):'")
    if size == 'S' or size == 'M' or size == 'L':
        print(size)
    else:
        continue
