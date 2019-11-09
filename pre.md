# Narrative

### Intro
There are a lot of thoughts when it comes to creating Pythonic code. The first being, "What is it?". You can think of Pythonic code as a program that seems natural through its simplicity or as an easy to understand solution to a complex problem. Clean or Pythonic code can make the difference in landing a job, getting a promotion, and establishing yourself as not just a programmer but an excellent programmer- someone other coders can work with. Sounds nice, right? So, how can you start turning your code into Pythonic code?

While many practices comprise clean code, one tool to achieve Pythonic code is called **List Comprehension**. Take the following mystery program as an example. Spend a few moments figuring out what this program does.

#### Mystery Program
```python

list_1 = ['what', 'is', 'the', 'code', 'word', 'for', 'clean', 'python', 'code']
list_2 = []
word = 'code'
count = 0
for x in list_1:
  if x == word:
    list_2.append(count)
  count += 1
print(list_2)

```

What is this code trying to accomplish? How long did it take you to figure that out? Where you able to figure out? These seemingly small questions can have a large impact on the day-to-day for a programmer. A lack of clean code can lead to disfunction in joint projects and frustration. Let's run this code and see if the output matches what you thought this program would do.


```python

[3,8]

```
We got a list with the intergers 3 and 8 inside. Interesting, this program is recording the index of each appearce of the string "code" in list_1. Let's first look at some pseudocode.

```python

for every item in list_1:
  if this item == word:
    add this item to list_2
```


Feel free to skip this  paragraph if you understand how mystery program works. This program iterates through list_1 and compares each element of list_1 to the variable **word**. If the element is equal to **word**, the program appends list_2 with **count**. We can see that **count** is keeping track of the iterators index position in list_1. **count** increases from 0 by one after each iteration of the loop. So, this program is recording the index of each appearce of **word** in list_1. We can see that the value of **word** "code" is located at index 3 and 8 in list_1. Remeber, lists always start from index 0 in python

#### Connection
Phew, that was a lot of code for such a straight forward task. At the end of this lesson, you will use **List Comprehension** to cut the mystery program's length in half. First, let's break down how to use **List Comprehension** step-by-step to better understand how we make the mystery program more Pythonic.
