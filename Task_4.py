def cacluate(num):
    a = []
    while True:
        num = input()
        if num == '':
            break
        a.append(num)
    f = 0
    y = 0
    for i in a:
        f = f + int(i)
        y += 1
    p = f / y
    d = []
    for i in a:
        if int(i) > p:
            d.append(i)
    kortage = {p: d}
    return kortage

print(cacluate(input()))


