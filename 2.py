#prime numbers upto n
def primeno(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num, end=" ")


start = int(input("Enter starting value"))

for i in range(start):
    primeno(i)
