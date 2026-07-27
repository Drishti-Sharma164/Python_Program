# 1. Write a Python program to create a set.

s = {10, 20, 30, 40, 50}
print("Set:", s)


# 2. Write a Python program to iteration over sets.

s = {10, 20, 30, 40}
for i in s:
    print(i)


# 3. Write a Python program to add member(s) in a set.

s = {10, 20, 30}
s.add(40)
s.update([50, 60])
print(s)


# 4. Write a Python program to remove item(s) from set.

s = {10, 20, 30, 40}
s.remove(20)
print(s)


# 5. Write a Python program to remove an item from a set if it is present in the set.

s = {10, 20, 30, 40}
if 20 in s:
    s.remove(20)
print(s)


# 6. Write a Python program to create an intersection of sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Intersection:", set1.intersection(set2))


# 7. Write a Python program to create a union of sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))


# 8. Write a Python program to create set difference.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
print("Difference:", set1.difference(set2))


# 9. Write a Python program to create a symmetric difference.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Symmetric Difference:", set1.symmetric_difference(set2))


# 10. Write a Python program to issubset and issuperset.

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print("Subset:", set1.issubset(set2))
print("Superset:", set2.issuperset(set1))


# 11. Write a Python program to create a shallow copy of sets.

s1 = {10, 20, 30}
s2 = s1.copy()

print("Original Set:", s1)
print("Copied Set:", s2)


# 12. Write a Python program to clear a set.

s = {10, 20, 30}
s.clear()
print(s)


# 13. Write a Python program to use of frozensets.

s = frozenset([10, 20, 30, 40])
print(s)


# 14. Write a Python program to find maximum and the minimum value in a set.

s = {25, 10, 50, 5, 35}

print("Maximum:", max(s))
print("Minimum:", min(s))


# 15. Write a Python program to find the length of a set.

s = {10, 20, 30, 40, 50}
print("Length of Set:", len(s))
