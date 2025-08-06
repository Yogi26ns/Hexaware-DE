# #Level-1
# 2.Write a program to check whether a number is even or odd.
x=int(input("Enter a number: "))
if x%2==0:
    print("Even")
else:
    print("Odd")
#
# # 3.Write a program to grade students based on marks:
marks = int(input("Enter a marks: "))
if marks>=90:
    print("A")
elif 75<=marks<89:
    print("B")
elif 74<=marks<=60:
    print("C")
else:
    print("D")
# # 4.Write a program to:
# #     Check if a number is positive
# #     If positive, check if it’s greater than 100
# #     Else, print "Positive but less than or equal to 100"
a=int(input("Enter a number: "))
if a>0:
    if a>100:
        print("Greater than 100")
    else:
        print("Positive,but less than or equal to 100")
else:
    print("Negative number")
# # Multiple if (Parallel Checks)
# # 5.Write a program to check whether a number is:
# Divisible by 2
# Divisible by 3
# Divisible by 5
# # (Don't use elif. Multiple if statements should run independently.)
num=int(input("Enter a number: "))
if num%2==0:
    print("Divisible by 2")
if num%3==0:
    print("Divisible by 3")
if num%5==0:
    print("Divisible by 5")

# # Level-2 Loops
# # 1.Write a program to print the first 10 natural numbers.
for i in range(1,11):
    print(i)
# # 2.Write a program to print numbers from 10 to 1 in reverse.
for i in range(10,0,-1):
    print(i)
# # 3.Write a program to print all even numbers between 1 and 20.
for even in range(2,21,2):
    print(even)
# # 4.Write a program to sum all natural numbers until the sum becomes greater than 100.
total=0
for i in range(1,100):
    total+=i
    if total>100:
        break
    print(total)
# #or
total=0
while True:
    #idk but i will try
    for i in range(1,100):
        total+=i
        if total>100:
            break
    print(total)
    False

# # level 3 jump
# # Write a program to find the first number divisible by 7 in the range 1 to 50 and stop the loop immediately.
for i in range(1,50):
    if i%7==0:
        print(i)
        break
#
# # Write a program to print numbers from 1 to 10 but skip number 5.
for i in range(1,11):
    if i == 5:
        continue
    print(i)
# # Write a program where you loop from 1 to 5, but if the number is 3, use pass (do nothing) and continue the loop.
for i in range(1,5):
    if i==3:
        pass
    print(i)
# # Loop from 1 to 30
# #
# # Skip multiples of 4 using continue
# #
# # Stop the loop if the number is greater than 20 using break
# #
# # If the number is 7, just pass and continue
# for i in range(1,30):
#     if i%4==0:
#         continue
#     if i>20:
#         break
#     if i==7:
#         pass
#
# Level 3 – Data Structure Coding Ladder
# -------------------------
# A. Lists
# -------------------------

# 1. Create a list of 5 numbers. Print the sum and average.
list=[1,2,3,4,5,1]
sum=0
for i in list:
    sum=sum+i
    mean=sum/len(list)
print(sum)
print(mean)
# 2. Remove the second element from the list.
list.pop(1)
# 3. Write a program to reverse the list without using [::-1].
print(list[::-1])
# 4. Find the maximum and minimum in the list without using built-in functions.
max=0
for i in list:
    if i>max:
        max=i
    print(max)
# 5. Write a program to count how many times a number appears in the list.
count=0
for i in list:
    if i==i:
        count+=1
    print(count)
# -------------------------
# B. Tuples
# -------------------------

# 6. Create a tuple of 5 numbers and print the sum.
t = (10, 20, 30, 40, 50)
print("Sum of tuple elements:", sum(t))

# 7. Try to update the second element of the tuple.
try:
    t[1] = 100
except TypeError as e:
    print("Error while updating tuple:", e)

# 8. Convert a tuple to a list → update an element → convert it back to a tuple.
t_list = list(t)
t_list[1] = 100
t_updated = tuple(t_list)
print("Updated tuple:", t_updated)

# -------------------------
# C. Strings
# -------------------------

# 9. Check if a string is a palindrome.
s = "madam"
if s == s[::-1]:
    print(f"'{s}' is a palindrome")
else:
    print(f"'{s}' is not a palindrome")

# 10. Count the number of vowels in a string.
s = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print("Number of vowels:", count)

# 11. Reverse a string without using [::-1].
s = "Python"
reversed_s = ''
for char in s:
    reversed_s = char + reversed_s
print("Reversed string:", reversed_s)

# 12. Remove all spaces from the string without using replace().
s = "H e l l o   W o r l d"
no_spaces = ''.join(c for c in s if c != ' ')
print("String without spaces:", no_spaces)

# -------------------------
# D. Dictionaries
# -------------------------

# 13. Create a dictionary of 3 key-value pairs and print all keys and values.
d = {'name': 'Alice', 'age': 25, 'city': 'Chennai'}
print("Keys:", d.keys())
print("Values:", d.values())

# 14. Write a program to update the value of a key.
d['age'] = 26
print("Updated dictionary:", d)

# 15. Write a program to delete a key from the dictionary.
del d['city']
print("Dictionary after deletion:", d)

# 16. Check if a key exists in the dictionary.
key_to_check = 'name'
if key_to_check in d:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")

# -------------------------
# E. Sets
# -------------------------

# 17. Create two sets → print union, intersection, difference.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)

# 18. Add a new element to a set.
set1.add(7)
print("Set after adding 7:", set1)

# 19. Remove an element from a set.
set1.discard(2)
print("Set after removing 2:", set1)

# 20. Write a program to remove duplicates from a list using a set.
lst = [1, 2, 2, 3, 4, 4, 5]
no_duplicates = list(set(lst))
print("List without duplicates:", no_duplicates)
