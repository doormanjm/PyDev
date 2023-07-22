d = {}

n=int(input("Enter the range of items for the dictonary:"))

for i in range(1,n+1):
    value = input('Enter any value? ')
    d[i] = value

print(d)