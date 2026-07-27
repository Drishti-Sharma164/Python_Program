# 1. Write a Python program to sum all the items in a list.  

s=[1,2,3,4,5]
print(sum(s))
  
# 2. Write a Python program to multiplies all the items in a list.

l = [2, 3, 4, 5]
m = 1
for i in l:
    m*= i
print("Product =", m)
  
# 3. Write a Python program to get the largest number from a list.

l=[1,7,3,4,5]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]    
print("largest number:",m)
  
# 4. Write a Python program to get the smallest number from a list.  

l=[1,7,3,4,5]
m=l[0]
for i in range(len(l)):
    if l[i]<m:
        m=l[i]    
print("smallest number:",m)
  
# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.  
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

l=['abc', 'xyz', 'aba', '1221']
c=0
for i in l:
    if len(i)>2 and i[0]==i[-1]:
        c=c+1
print(c)

6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.  
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
  
# 7. Write a Python program to remove duplicates from a list.  

l=[1,2,3,4,3,4]
for i in l:
    if l.count(i)>1:
        l.remove(i)
print(l)

l = [1, 2, 3, 4, 3, 4]
new = []
for i in l:
    if i not in new:
        new.append(i)
print(new)
  
# 8. Write a Python program to check a list is empty or not. 

l = [1, 2]
if l == []:
    print("Empty List")
else:
    print("List is not empty")
  
# 9. Write a Python program to clone or copy a list.  

l = [1, 2]
copy_list = l.copy()
print(copy_list)
  
# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 

l = ["My", "Name", "is", "drishti", "sharma"]
new = []
n = int(input("Enter the size of word: "))
for i in l:
    if len(i) > n:
        new.append(i)
print(new)
  
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.  

l1=input("Enter the list:").split()
l2=input("Enter the list:")).split()
f=False
for i in l1:
    if i in l2:
        f=True
        break
print(f)
  
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.  
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in [5, 4, 0]:
    l.pop(i)
print(l)

  
# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.  
  
# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.  

l = [1, 2, 3, 4, 5, 6]
new = []
for i in l:
    if i % 2 != 0:
        new.append(i)
print(new)
  
# 15. Write a Python program to shuffle and print a specified list.  

import random
l = [1, 2, 3, 4, 5]
random.shuffle(l)
print(l)
  
# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).  

l = []
for i in range(1, 31):
    l.append(i * i)
print("First 5 elements:", l[:5])
print("Last 5 elements:", l[-5:])
  
# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).  

l = []
for i in range(1, 31):
    l.append(i * i)
print(l[5:])

# 18. Write a Python program to generate all permutations of a list in Python.  
  
# 19. Write a Python program to get the difference between the two lists.  

l1 = [1, 2, 3, 4, 5]
l2 = [0, 1, 3, 4, 7]
l3 = []
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)
  
# 20. Write a Python program access the index of a list.  

l = [10, 20, 30, 40]
for i in range(len(l)):
    print("Index:", i, "Element:", l[i])

  
# 21. Write a Python program to convert a list of characters into a string.  

l = ['D', 'r', 'i', 's', 'h', 't', 'i']
s = "".join(l)
print(s)

# 22. Write a Python program to find the index of an item in a specified list.  

l = [10, 20, 30, 40]
item = int(input("Enter item: "))
print(l.index(item))

# 23. Write a Python program to flatten a shallow list.  

l = [[1, 2], [3, 4], [5, 6]]
new = []
for i in l:
    for j in i:
        new.append(j)
print(new)
  
# 24. Write a Python program to append a list to the second list.  

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l2.append(l1)
print(l2)
  
# 25. Write a Python program to select an item randomly from a list.  

import random
l = [10, 20, 30, 40, 50]
print(random.choice(l))
  
# 26. Write a python program to check whether two lists are circularly identical.

l1 = [1, 2, 3, 4]
l2 = [3, 4, 1, 2]

if len(l1) == len(l2):
    s = l1 + l1
    if str(l2) in str(s):
        print("Circularly Identical")
    else:
        print("Not Circularly Identical")
  
# 27. Write a Python program to find the second smallest number in a list.  

l = [5, 2, 8, 1, 3]
l.sort()
print("Second Smallest =", l[1])
  
# 28. Write a Python program to find the second largest number in a list.

l = [5, 2, 8, 1, 3]
l.sort()
print("Second Largest =", l[-2])
  
# 29. Write a Python program to get unique values from a list.  

l = [1, 2, 3, 2, 4, 1, 5]
new = []
for i in l:
    if i not in new:
        new.append(i)
print(new)
  
# 30. Write a Python program to get the frequency of the elements in a list.  

l = [1, 2, 2, 3, 1, 4, 2]
for i in l:
    print(i, ":", l.count(i))
  
# 31. Write a Python program to count the number of elements in a list within a specified range.  

l = [2, 5, 8, 10, 15, 20]
count = 0
a = int(input("Enter starting range: "))
b = int(input("Enter ending range: "))
for i in l:
    if a <= i <= b:
        count += 1
print(count)
  
# 32. Write a Python program to check whether a list contains a sublist.  

l = [1, 2, 3, 4, 5]
sub = [2, 3]
if str(sub) in str(l):
    print("Sublist found")
else:
    print("Sublist not found")
  
# 33. Write a Python program to generate all sublists of a list.  

l = [1, 2, 3]
for i in range(len(l)):
    for j in range(i + 1, len(l) + 1):
        print(l[i:j])
  
# 34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.  
# Note https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes  


# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.  
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

l = ['p', 'q']
n = 5
new = []
for i in range(1, n + 1):
    for j in l:
        new.append(j + str(i))
print(new)
  
# 36. Write a Python program to get variable unique identification number or string.

a = [1, 2, 3]
print(id(a))

  
# 37. Write a Python program to find common items from two lists.  

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
for i in l1:
    if i in l2:
        print(i)
      
#38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.  
#Sample list: [0,1,2,3,4,5]
#Expected Output: [1, 0, 3, 2, 5, 4]


#39. Write a Python program to convert a list of multiple integers into a single integer.  
#Sample list: [11, 33, 50]
#Expected Output: 113350

l = [11, 33, 50]
s = ""
for i in l:
    s = s + str(i)
print(int(s))
  
# 40. Write a Python program to split a list based on first character of word.  

l = ["apple", "ant", "ball", "bat", "cat"]
d = {}
for i in l:
    if i[0] not in d:
        d[i[0]] = []
    d[i[0]].append(i)
print(d)
  
# 41. Write a Python program to create multiple lists. 

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = [10.5, 20.5]
print(l1)
print(l2)
print(l3)
  
#42. Write a Python program to find missing and additional values in two lists.  
#Sample data : Missing values in second list: b,a,c
#Additional values in second list: g,h

l1 = ['a', 'b', 'c', 'd', 'e', 'f']
l2 = ['d', 'e', 'f', 'g', 'h']

print("Missing values:")
for i in l1:
    if i not in l2:
        print(i)

print("Additional values:")

for i in l2:
    if i not in l1:
        print(i)
      
#43. Write a Python program to split a list into different variables.  

l = [10, 20, 30]
a, b, c = l
print(a)
print(b)
print(c)

#44. Write a Python program to generate groups of five consecutive numbers in a list.  

for i in range(1, 21, 5):
    print(list(range(i, i + 5)))

#45. Write a Python program to convert a pair of values into a sorted unique array.  
  
#46. Write a Python program to select the odd items of a list.  

l = [10, 20, 30, 40, 50, 60]
for i in range(1, len(l), 2):
    print(l[i])
  
#47. Write a Python program to insert an element before each element of a list.  

l = [1, 2, 3]
new = []
for i in l:
    new.append(0)
    new.append(i)
print(new)

#48. Write a Python program to print a nested lists (each list on a new line) using the print() function.  

l = [[1, 2], [3, 4], [5, 6]]
for i in l:
    print(i)
  
#49. Write a Python program to convert list to list of dictionaries.  
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
  
#50. Write a Python program to sort a list of nested dictionaries.  
  
51. Write a Python program to split a list every Nth element.  
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
  
52. Write a Python program to compute the similarity between two lists.  
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
  
53. Write a Python program to create a list with infinite elements.  
  
54. Write a Python program to concatenate elements of a list.  
  
55. Write a Python program to remove key values pairs from a list of dictionaries.  
  
56. Write a Python program to convert a string to a list.  
  
57. Write a Python program to check if all items of a list is equal to a given string.  
  
58. Write a Python program to replace the last element in a list with another list.  
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
  
59. Write a Python program to check if the n-th element exists in a given list.  
  
60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.  
  
61. Write a Python program to create a list of empty dictionaries.  
  
62. Write a Python program to print a list of space-separated elements.  
  
63. Write a Python program to insert a given string at the beginning of all items in a list.  
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
  
64. Write a Python program to iterate over two lists simultaneously.  
  
65. Write a Python program to access dictionary keys element by index.  
  
66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.  
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
  
67. Write a Python program to find all the values in a list are greater than a specified number.  
  
68. Write a Python program to extend a list without append.  
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]
  
69. Write a Python program to remove duplicates from a list of lists.  
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
  
70. Write a Python program to get the depth of a dictionary.  
  
71. Write a Python program to check if all dictionaries in a list are empty or not.  
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
  
