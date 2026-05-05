# Given a=[1,2,4,2,5,2,6], remove all 2s and print the final list.
a = [1, 2, 4, 2, 5, 2, 6]

while 2 in a:
    a.remove(2)

print(a)  
# Given nums=[9,2,11,7,11,3], find the second largest distinct value using loops.
nums = [9, 2, 11, 7, 11, 3]

sorted_nums = sorted(set(nums), reverse=True)  

second = sorted_nums[1]

print("Second largest  =", second)  
# Given a=[10,20,30,40,50], rotate left by 1: result should be [20,30,40,50,10].
a = [10, 20, 30, 40, 50]

first = a.pop(0)   
a.append(first)  

print(a)  

# Given a=[1,2,3,4,5], insert value 99 at index k (input k). Do not use insert().
a = [1, 2, 3, 4, 5]

k = int(input("Enter index k (0..5): "))
value = 99

a = a[:k] + [value] + a[k:]

print(a)
# Given a=[5,6,7,8,9,10], delete the element at index k using shifting + final pop() 
a = [5, 6, 7, 8, 9, 10]

k = int(input("Enter index k (0..5): "))

a = a[:k] + a[k+1:]

print(a)

# Input a line of text. Split into words. Print the longest word and its length. 

# -

# Given a sentence, split into words, then join using " | " as separator and print.
s = input("Enter sentence: ")

words = s.split()

print(" | ".join(words))

# Given a=[3,3,2,3,1,2,4,4], create a new list of unique elements preserving order. 
a = [3, 3, 2, 3, 1, 2, 4, 4]

c = []
b = []

for x in a:
    if x not in b:
        b.append(x)
        c.append(x)

print(c)  



# Given a=[1,1,1,2,2,3,4,4], print each distinct value with its frequency
a = [1, 1, 1, 2, 2, 3, 4, 4]

b = []

for x in a:
    if x not in b:
        print(x, "->", a.count(x))
        b.append(x)

# Sort a=[8,3,5,2,9,1] in ascending order using bubble sort (no sort()). 
 a = [8, 3, 5, 2, 9, 1]

n = len(a)

for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)  
