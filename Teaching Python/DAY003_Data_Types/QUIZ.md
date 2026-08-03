# Python Quiz – Data Types, Operators & Type Conversion

Test your understanding of Python basics. Answers and explanations are provided after each question.

---

# Question 1

### Which statement below is **incorrect**?

- A. `932` is an Integer
- B. `"False"` is a Boolean
- C. `857.25` is a Float
- D. `"523"` is a String

## ✅ Answer

**B. `"False"` is a Boolean**

### Explanation

- `932` → Integer ✔
- `"False"` → **String**, because it is inside quotes ❌
- `857.25` → Float ✔
- `"523"` → String ✔

Remember:

```python
False      # Boolean
"False"    # String
```

---

# Question 2

### What is the data type of the variable?

```python
mystery = 734_529.678
```

- A. Integer
- B. String
- C. Qurtle
- D. Float

## ✅ Answer

**D. Float**

### Explanation

Python allows underscores in numbers to improve readability.

```python
734_529.678
```

is the same as

```python
734529.678
```

Since it contains a decimal point, it is a **float**.

---

# Question 3

### What will this code print?

```python
street_name = "Abbey Road"

print(street_name[4] + street_name[7])
```

- A. eR
- B. en
- C. yo
- D. ya

## ✅ Answer

**B. en**

### Explanation

```
Abbey Road

Index

A  b  b  e  y     R  o  a  d
0  1  2  3  4 5  6  7  8  9
```

```
street_name[4] = y
street_name[7] = o
```

Output:

```text
yo
```

> **Correction:** The correct output is actually **`yo`**, so the correct answer is **C**. (The original options contain an incorrect answer key.)

---

# Question 4

### What will this code print?

```python
print(6 + 4 / 2 - (1 * 2))
```

- A. 3
- B. 6.0
- C. 8.0
- D. 5

## ✅ Answer

**B. 6.0**

### Explanation

Follow PEMDAS/BODMAS.

```
4 / 2 = 2.0

1 * 2 = 2

6 + 2.0 - 2

= 6.0
```

---

# Question 5

### What is the data type of variable `a`?

```python
a = int("5") / int(2.7)
```

- A. int
- B. float
- C. str
- D. bool

## ✅ Answer

**B. float**

### Explanation

```
int("5") = 5

int(2.7) = 2

5 / 2 = 2.5
```

Division (`/`) always returns a **float**.

---

# Question 6

### Which block of code gives an error?

### Block 1

```python
name = input("What is your name?")
print(f"Hello, {name}")
```

### Block 2

```python
name = input("What is your name?")
print("Hello, " + name)
```

### Block 3

```python
age = 12
print(f"You are {age} years old")
```

### Block 4

```python
age = 12
print("You are " + age + " years old")
```

## ✅ Answer

**Block 4**

### Explanation

`age` is an integer.

Python cannot join a string and an integer using `+`.

This causes

```text
TypeError
```

Correct ways:

```python
print("You are " + str(age) + " years old")
```

or

```python
print(f"You are {age} years old")
```

---

# Additional Practice Questions

## Question 7

What is the output?

```python
print(type(True))
```

- A. `<class 'bool'>`
- B. `<class 'str'>`
- C. `<class 'int'>`
- D. `<class 'float'>`

### ✅ Answer

**A**

---

## Question 8

What is the output?

```python
print(len("Python"))
```

- A. 5
- B. 6
- C. 7
- D. Error

### ✅ Answer

**B**

---

## Question 9

What is the output?

```python
print("Python"[2])
```

- A. y
- B. P
- C. t
- D. h

### ✅ Answer

**C**

Explanation

```
P y t h o n
0 1 2 3 4 5
```

---

## Question 10

What is the output?

```python
print("Python"[-1])
```

- A. P
- B. h
- C. n
- D. Error

### ✅ Answer

**C**

---

## Question 11

What is the output?

```python
print(5 // 2)
```

- A. 2
- B. 2.5
- C. 3
- D. 1

### ✅ Answer

**A**

---

## Question 12

What is the output?

```python
print(5 % 2)
```

- A. 0
- B. 1
- C. 2
- D. 2.5

### ✅ Answer

**B**

---

## Question 13

What is the output?

```python
print(2 ** 4)
```

- A. 8
- B. 16
- C. 12
- D. 6

### ✅ Answer

**B**

---

## Question 14

What is the output?

```python
print(str(100) + str(50))
```

- A. 150
- B. 10050
- C. Error
- D. 50

### ✅ Answer

**B**

---

## Question 15

What is the output?

```python
print(int("25") + 5)
```

- A. 255
- B. 30
- C. Error
- D. 20

### ✅ Answer

**B**

---

## Question 16

Which line produces an error?

- A.

```python
print(int("123"))
```

- B.

```python
print(float("3.14"))
```

- C.

```python
print(int("Python"))
```

- D.

```python
print(str(100))
```

### ✅ Answer

**C**

---

## Question 17

What is the output?

```python
print(bool(""))
```

- A. True
- B. False
- C. Error
- D. None

### ✅ Answer

**B**

---

## Question 18

What is the output?

```python
print(round(8.7654, 2))
```

- A. 8
- B. 8.76
- C. 8.77
- D. 9

### ✅ Answer

**C**

---

## Question 19

What is the output?

```python
print(type(10 / 2))
```

- A. int
- B. float
- C. bool
- D. str

### ✅ Answer

**B**

---

## Question 20

Which function returns the data type of a variable?

- A. `len()`
- B. `print()`
- C. `type()`
- D. `str()`

### ✅ Answer

**C**

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| `str` | Text |
| `int` | Whole numbers |
| `float` | Decimal numbers |
| `bool` | True / False |
| `len()` | Returns length |
| `type()` | Returns data type |
| `str()` | Converts to string |
| `int()` | Converts to integer |
| `/` | Division (float) |
| `//` | Floor division |
| `%` | Modulus (remainder) |
| `**` | Exponentiation |
| `+` | Adds numbers / joins strings |

---

# Memory Tips

- **Quotes → String**
- **No quotes → Number or Boolean**
- **`/` always returns a float**
- **`+` joins strings but adds numbers**
- **Python indexing starts at 0**
- **Negative indexing starts from -1**
- **`len()` works on strings, lists, tuples, etc.—not integers**
- **Use `type()` whenever you're unsure of a variable's data type**
