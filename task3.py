def fibonacci_series(n):
    series = []
    a = 0
    b = 1   
    for i in range(n):
        series.append(a)
        c = a + b
        a = b
        b = c
    return series

n=int(input("Enter the required range: "))
if n < 0:
    print("Incorrect input")
else:
    print(fibonacci_series(n))
