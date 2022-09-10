x = input("Enter the words:")

n = len(x)
print(n)

if n == 1 or n == 2:
    print(x)
elif n % 2 != 0:
    m = (n+1)//2
    print(x[m-1])
elif n % 2 == 0:
    m = n//2
    print(x[m-1:m+1])



