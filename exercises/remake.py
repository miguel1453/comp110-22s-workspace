x: str = "tarheel"
y: int = 2
z = len(x) - 3

y = y ** 2 
x = x[z - 1] + x[y] + str(y)

print(x)
print(y % 4)
print(z)