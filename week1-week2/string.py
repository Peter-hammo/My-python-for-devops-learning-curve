#examples are follows:

#Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)


#string length
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

#uppercase and lowercase
text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#replacing
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)


#spltting
text = "Python is awesome"
words = text.split()
print("Words:", words)

#strip text
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)


#substring
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")







