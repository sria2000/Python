# Python Lists - MCQ Practice Questions and Answers

## Topic: Python Lists, Indexing, Negative Indexing, Append, Nested Lists

---

# Question 1: Accessing List Items Using Index

### Question:

Given the following list:

```python
fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears"
]
```

Which line of code will give you `"Apples"`?

### Options:

A)

```python
fruits[3]
```

B)

```python
fruits[4]
```

C)

```python
fruits.Apples()
```

D)

```python
fruits[-5]
```

E)

```python
fruits[-4]
```

---

## Answer:

✅ **D) `fruits[-5]`**

---

## Explanation:

Python list indexes start from **0**.

| Positive Index | Negative Index | Value |
|---|---|---|
| 0 | -7 | Strawberries |
| 1 | -6 | Nectarines |
| 2 | -5 | Apples |
| 3 | -4 | Grapes |
| 4 | -3 | Peaches |
| 5 | -2 | Cherries |
| 6 | -1 | Pears |

So:

```python
fruits[-5]
```

returns:

```
Apples
```

---

# Question 2: Updating and Appending Items

### Question:

Given the code:

```python
fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears"
]

fruits[-1] = "Melons"

fruits.append("Lemons")

print(fruits)
```

What will be printed?

---

## Options:

A)

```python
[
"Strawberries",
"Nectarines",
"Apples",
"Grapes",
"Peaches",
"Cherries",
"Lemons"
]
```

B)

```python
[
"Strawberries",
"Nectarines",
"Apples",
"Grapes",
"Peaches",
"Cherries",
"Pears",
"Lemons"
]
```

C)

```python
[
"Strawberries",
"Nectarines",
"Apples",
"Grapes",
"Peaches",
"Cherries",
"Pears",
"Melons",
"Lemons"
]
```

D)

```python
[
"Strawberries",
"Nectarines",
"Apples",
"Grapes",
"Peaches",
"Cherries",
"Melons",
"Lemons"
]
```

---

## Answer:

✅ **D**

```python
[
"Strawberries",
"Nectarines",
"Apples",
"Grapes",
"Peaches",
"Cherries",
"Melons",
"Lemons"
]
```

---

## Explanation:

Initially:

```
Index 6 = Pears
```

This line:

```python
fruits[-1] = "Melons"
```

changes the last item.

Before:

```
Pears
```

After:

```
Melons
```

Then:

```python
fruits.append("Lemons")
```

adds a new item at the end.

Final list:

```
Strawberries
Nectarines
Apples
Grapes
Peaches
Cherries
Melons
Lemons
```

---

# Question 3: Nested Lists

### Question:

Given:

```python
fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears"
]

vegetables = [
    "Spinach",
    "Kale",
    "Tomatoes",
    "Celery",
    "Potatoes"
]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
```

What will be printed?

---

## Options:

A)

```
Spinach
```

B)

```
Strawberries
```

C)

```
Kale
```

D)

```python
["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
```

E)

```
Nectarines
```

---

## Answer:

✅ **C) Kale**

---

## Explanation:

Nested list:

```python
dirty_dozen = [fruits, vegetables]
```

Structure:

```
dirty_dozen

[0] fruits
[1] vegetables
```

First index:

```python
dirty_dozen[1]
```

selects:

```
vegetables
```

Second index:

```python
vegetables[1]
```

selects:

```
Kale
```

Therefore:

```python
dirty_dozen[1][1]
```

Output:

```
Kale
```

---

# Additional MCQ Practice Questions

---

# Question 4: List Length

What will this print?

```python
numbers = [10,20,30,40,50]

print(len(numbers))
```

Options:

A) 4  
B) 5  
C) 6  
D) Error  

## Answer:

✅ B) 5

Explanation:

`len()` returns the number of items.

---

# Question 5: Last Item in List

What is the output?

```python
colors = [
    "Red",
    "Blue",
    "Green",
    "Yellow"
]

print(colors[-1])
```

Options:

A) Red  
B) Blue  
C) Green  
D) Yellow  

## Answer:

✅ D) Yellow

Explanation:

`-1` always represents the last item.

---

# Question 6: append() Method

What will be printed?

```python
animals = [
    "Dog",
    "Cat"
]

animals.append("Horse")

print(animals)
```

Options:

A)

```python
["Dog","Cat"]
```

B)

```python
["Horse","Dog","Cat"]
```

C)

```python
["Dog","Cat","Horse"]
```

D) Error

## Answer:

✅ C)

Explanation:

`append()` adds an item at the end.

---

# Question 7: extend() Method

What is the output?

```python
numbers = [1,2,3]

numbers.extend([4,5])

print(numbers)
```

Options:

A)

```python
[1,2,3,[4,5]]
```

B)

```python
[1,2,3,4,5]
```

C)

```python
[4,5,1,2,3]
```

D) Error

## Answer:

✅ B)

Explanation:

`extend()` adds each item individually.

---

# Question 8: append vs extend

What is the output?

```python
numbers = [1,2,3]

numbers.append([4,5])

print(numbers)
```

Options:

A)

```python
[1,2,3,4,5]
```

B)

```python
[1,2,3,[4,5]]
```

C)

```python
[4,5]
```

D) Error

## Answer:

✅ B)

Explanation:

`append()` adds the entire list as one item.

---

# Question 9: Changing List Values

What will print?

```python
cars = [
    "BMW",
    "Audi",
    "Tesla"
]

cars[1] = "Mercedes"

print(cars)
```

Options:

A)

```python
["BMW","Audi","Tesla"]
```

B)

```python
["BMW","Mercedes","Tesla"]
```

C)

```python
["Mercedes","Audi","Tesla"]
```

D) Error

## Answer:

✅ B)

Explanation:

Lists are mutable, so values can be changed.

---

# Question 10: Nested List Access

What will print?

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[2][1])
```

Options:

A) 7  
B) 8  
C) 9  
D) 5  

## Answer:

✅ B) 8

Explanation:

First:

```python
matrix[2]
```

selects:

```
[7,8,9]
```

Then:

```python
[1]
```

selects:

```
8
```

---

# Key Exam Points

| Concept | Example | Result |
|---|---|---|
| First item | `list[0]` | First value |
| Last item | `list[-1]` | Last value |
| Change value | `list[2]="New"` | Updates item |
| Add item | `append()` | Adds one item |
| Add multiple | `extend()` | Adds multiple items |
| Nested list | `list[1][2]` | Access inside list |
| Count items | `len(list)` | Number of elements |
