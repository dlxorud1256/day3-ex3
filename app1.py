for n in range(1, 101):
    if n % 2 == 0 and n % 5 == 0:
        print("2와 5의 배수입니다")
    elif n % 2 == 0:
        print("2의 배수입니다")
    elif n % 5 == 0:
        print("5의 배수입니다")
    else:
        print(n)
