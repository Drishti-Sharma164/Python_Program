# 1. Count how many of each vowel (a, e, i, o, u) there are in a text string, and print the count for each vowel with a single formatted string. Remember that vowels can be both lower and uppercase.
text = input("Enter a text: ")
a = text.lower().count('a')
e = text.lower().count('e')
i = text.lower().count('i')
o = text.lower().count('o')
u = text.lower().count('u')
print(f"a = {a}, e = {e}, i = {i}, o = {o}, u = {u}")

#2. Below is a text with several characters enclosed in square brackets [] and Scan the text and print out all characters which are between square brackets.
text = "ab[m]cd[on]ef"
t = False
for i in text:
    if i == '[':
        t = True
    elif i == ']':
        t = False
    elif t :
        print(i , end="")

#3. Print a line of all the capital letters "A" to "Z". Below it, print a line of the letters that are 13 positions in the alphabet away from the letters that are above them. E.g., below the "A" you print an "N", below the "B" you print an "O", etcetera. You have to consider the alphabet to be circular, i.e., after the "Z", it loops back to the "A" again.
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a)

for i in a:
    p= a.index(i)
    np= (p+ 13) % 26
    print(a[np], end="")

#4.  In the text below, count how often the word “wood” occurs (using pro-gram code, of course). Capitals and lower case letters may both be used, and you have to consider that the word “wood” should be a separate word, and not part of another word. Hint: If you did the exercises from this chapter, you already developed a function that “cleans” a text. Combining that function with the split() function more or less solves the problem for you.
#text = """How much wood would a woodchuck chuck If a woodchuck could chuck wood?
#He would chuck , he would , as much as he could ,
#And chuck as much as a woodchuck would
#If a woodchuck could chuck wood."""

text = """How much wood would a woodchuck chuck If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""
 
c = 0
words = text.lower().split()

for i in words:
    i = i.strip(".,?!")
    if i == "wood":
        c += 1
print("Number of times 'wood' occurs:", c)

#Write a program that takes a string and produces a new string that con-tains the exact characters that the first string contains, but in order of their ASCII-codes. For instance, the string "Hello, world!" should be turned into " !,Hdellloorw". This is relatively easy to do with list functions, which will be introduced in a future chapter, but for now try to do it with string manipulation functions alone.
text = input("Enter a string: ")
a = ""
while text != "":
    s= min(text)
    a+= s
    text = text.replace(s, "", 1)
print(a)

#Typical autocorrect functions are the following: (1) if a word starts with two capitals, followed by a lower-case letter, the second capital is made lower case; (2) if a sentence contains a word that is immediately followed by the same word, the second occurrence is removed; (3) if a sentence starts with a lower-case letter, that letter is turned into a capital; (4) if a word consists entirely of capitals, except for the first letter which is lower case, then the case of the letters in the word is reversed; and (5) if the sentence contains the name of a day (in English) which does not start with a capital, the first letter is turned into a capital. Write a program that takes a sentence and makes these auto-corrections. Test it out on the string below.

#sentence = "as it turned out our aRTHUR BElling was was to change every sunday we ' d hurry along to and Jam ..."
#chance meeting with REverend \ our whole way of life , and \ St lOONY up the Cream BUn \

s = """as it turned out our aRTHUR BElling was was to change every sunday we'd hurry along to and Jam a chance meeting with REverend our whole way of life and St lOONY up the Cream BUn"""
days = ("monday", "tuesday", "wednesday", "thursday","friday", "saturday", "sunday")
w = s.split()
r = []
for word in w:

    # Rule 1
    if len(word) >= 3:
        if word[0].isupper() and word[1].isupper() and word[2].islower():
            word = word[0] + word[1].lower() + word[2:]

    # Rule 4
    if len(word) > 1:
        if word[0].islower() and word[1:].isupper():
            word = word[0].upper() + word[1:].lower()

    # Rule 5
    if word.lower() in days:
        word = word.capitalize()

    # Rule 2
    if len(r) == 0 or r[-1].lower() != word.lower():
        r.append(word)

s = " ".join(r)

# Rule 3
if s[0].islower():
    s = s[0].upper() + s[1:]

print(s)

// Assigment - 02 
// 1. Write a Python program to calculate the length of a string. 

s = input("Enter a string: ")
count = 0
for i in s:
    count += 1
print("Length =", count)

// 2. Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

s = input("Enter a string: ")
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

// 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String

s = input("Enter a string: ")
if len(s) < 2:
    print("Empty String")
else:
    print(s[:2] + s[-2:])

// 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Sample String : 'restart'
Expected Result : 'resta$t'

s = input("Enter a string: ")
first = s[0]
new = first + s[1:].replace(first, "$")
print(new)

// 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.  
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

a = input("Enter first string: ")
b = input("Enter second string: ")
n1 = b[:2] + a[2:]
n2 = a[:2] + b[2:]
print(n1, n2)

// 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.  
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'

s = input("Enter a string: ")
if len(s) < 3:
    print(s)
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "ing")


// 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'

s = input("Enter a sentence: ")
n = s.find("not")
p = s.find("poor")

if n != -1 and p != -1 and n < p:
    s = s[:n] + "good" + s[p+4:]

print(s)
