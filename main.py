def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)
#Proportional O(n), O(n2), O(n*n)
#It doesnt matter the numbre of n, it will always be O(n)
#O(n*n) its less efficient, cause its not a straight line
