
x = int(input("Enter an integer: "))
ans = 0

while ans ** 3 < x:
    ans = ans + 1
if ans ** 3 != x:
    print(str(x) + " is not a perfect cube root")
else:
    print("Cube root of x " + str(x) + " is "  + str(ans))