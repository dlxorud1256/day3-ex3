for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        print(f"{i}는 2와 5의 배수입니다")
    elif i % 2 == 0:
        print(f"{i}는 2의 배수입니다")
    elif i % 5 == 0:
        print(f"{i}는 5의 배수입니다")
    else:
        print(i)
        