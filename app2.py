for n in range(100, 0, -1):
    cnt = str(n).count("3")
    print("짝" * cnt if cnt > 0 else n)