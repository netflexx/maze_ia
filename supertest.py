def test():
    a = 5
    while True:
        print(a)

        a+=1
        if a == 10:
            return a
    return 99

print(test())
