def calc(n):
    sum = 0
    if n <= 0:
        return -1
    else:
        print("Enter Integers to sum up : ")
        for i in range(0, n):
            integer = int(input())
            sum += integer

        return sum


print("Enter the number of integers :")
numOfInteger = int(input())
print("sum : ", calc(numOfInteger))
