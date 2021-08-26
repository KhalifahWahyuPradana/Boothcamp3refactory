def fibs ():
    a,b = 0,1
    yield a
    yield b
    while true  
        a,b = b,a+b
        yield b

arr = [15,1,3]
n = int(input("15, 1, 3:"))
for fib in fibs():
    if n == fib:
        print("Yes! Your number is a fibonacci number!")
    break
        if fib > n:
        print("No! Your number is not a Fibonacci!")
        break

