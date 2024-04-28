def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#print_items(10)
#Proportional O(n), O(n2), O(n*n)
#It doesnt matter the numbre of n, it will always be O(n)
#O(n*n) its less efficient, cause its not a straight line
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
#print_items(10)
#O(n'2 + n)
#n'2 is the dominant term, so we stay with it
#n is the no dominant term, insignificant

def add_items(n):
    return n + n
#O(1) even if we have many of the same constant, will remain constant
#Most efficient Big O
#The O(log n) is the second most efficient, but there is also O(nlog n), some sorting algorithm and most efficient on it

def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
#O(a) + O(b) = O(a+b) the most simple way to simplify on different terms
#When in a list we add a new thing, we can pop it without the number, just pop
#But if we pop(0), its remove, so the whole rest of list re-index
#If we want to insert(0,11), we are gonna index the whole list, and the add 11 to 0
#This list is still 0(n) even if we add new things on the middle or reinsert things, but if we add a new number AT THE END it will be O(1)


