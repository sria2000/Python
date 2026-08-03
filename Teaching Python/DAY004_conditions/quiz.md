# Python MCQs - Conditional Statements & Logical Operators

Test your understanding of Python conditional statements, comparison operators, and logical operators.

---

# Question 1

### What will the following code evaluate to?

```python
not 5 == 5
```

- A. True
- B. False
- C. Syntax Error

## ✅ Answer

**B. False**

### Explanation

```
5 == 5

True

not True

False
```

---

# Question 2

### What will the following code evaluate to?

```python
False or True or False
```

- A. True
- B. False
- C. Syntax Error

## ✅ Answer

**A. True**

### Explanation

The **OR** operator returns **True** if **at least one** condition is True.

```
False OR True OR False

↓

True
```

---

# Question 3

### What will the following code print?

```python
a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")
```

- A. A
- B. B
- C. C

## ✅ Answer

**B. B**

### Explanation

```
a >= b

5 >= 7

False
```

First condition

```
False and True

↓

False
```

Move to the `elif`

```
not False and True

↓

True and True

↓

True
```

Output

```text
B
```

---

# Additional Practice Questions

---

# Question 4

What will this print?

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Child")
```

- A. Adult
- B. Child
- C. Error

## ✅ Answer

**A. Adult**

---

# Question 5

What is the output?

```python
10 > 5 and 3 < 1
```

- A. True
- B. False

## ✅ Answer

**B. False**

### Explanation

```
10 > 5

True

3 < 1

False

True and False

↓

False
```

---

# Question 6

What is the output?

```python
10 > 5 or 3 < 1
```

- A. True
- B. False

## ✅ Answer

**A. True**

---

# Question 7

What will this print?

```python
print(not False)
```

- A. True
- B. False

## ✅ Answer

**A. True**

---

# Question 8

What will this print?

```python
x = 20

if x < 10:
    print("A")
elif x < 30:
    print("B")
else:
    print("C")
```

- A. A
- B. B
- C. C

## ✅ Answer

**B. B**

---

# Question 9

What is the output?

```python
print(5 != 5)
```

- A. True
- B. False

## ✅ Answer

**B. False**

---

# Question 10

What will this print?

```python
print(5 == 5)
```

- A. True
- B. False

## ✅ Answer

**A. True**

---

# Question 11

What is the output?

```python
print(5 <= 4)
```

- A. True
- B. False

## ✅ Answer

**B. False**

---

# Question 12

What will this print?

```python
score = 95

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

- A. A
- B. B
- C. C

## ✅ Answer

**A. A**

---

# Question 13

What is the output?

```python
print(True and True)
```

- A. True
- B. False

## ✅ Answer

**A. True**

---

# Question 14

What is the output?

```python
print(False and True)
```

- A. True
- B. False

## ✅ Answer

**B. False**

---

# Question 15

What is the output?

```python
print(True or False)
```

- A. True
- B. False

## ✅ Answer

**A. True**

---

# Question 16

What is the output?

```python
print(False or False)
```

- A. True
- B. False

## ✅ Answer

**B. False**

---

# Question 17

What will this print?

```python
x = 5

if x > 10:
    print("A")
else:
    print("B")
```

- A. A
- B. B

## ✅ Answer

**B. B**

---

# Question 18

What will this print?

```python
x = 8

if x > 5:
    if x < 10:
        print("Inside")
```

- A. Inside
- B. Error
- C. Nothing

## ✅ Answer

**A. Inside**

---

# Question 19

Which comparison operator means **Not Equal To**?

- A. `==`
- B. `!=`
- C. `>=`
- D. `<>`

## ✅ Answer

**B. `!=`**

---

# Question 20

What will this print?

```python
print(not (3 > 2))
```

- A. True
- B. False

## ✅ Answer

**B. False**

### Explanation

```
3 > 2

↓

True

not True

↓

False
```

---

# Question 21

What will this print?

```python
x = 15

if x > 10 and x < 20:
    print("Yes")
else:
    print("No")
```

- A. Yes
- B. No

## ✅ Answer

**A. Yes**

---

# Question 22

What will this print?

```python
x = 25

if x < 20 or x > 30:
    print("Yes")
else:
    print("No")
```

- A. Yes
- B. No

## ✅ Answer

**B. No**

---

# Question 23

What will this print?

```python
age = 15

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

- A. Adult
- B. Teenager
- C. Child

## ✅ Answer

**B. Teenager**

---

# Question 24

Which keyword is used to check another condition if the previous `if` condition is False?

- A. `otherwise`
- B. `elif`
- C. `then`
- D. `switch`

## ✅ Answer

**B. `elif`**

---

# Question 25

Which keyword executes when all previous conditions are False?

- A. `default`
- B. `else`
- C. `elif`
- D. `finally`

## ✅ Answer

**B. `else`**

---

# Quick Revision

## Comparison Operators

| Operator | Meaning |
|-----------|---------|
| `==` | Equal To |
| `!=` | Not Equal To |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater Than or Equal To |
| `<=` | Less Than or Equal To |

---

## Logical Operators

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses a Boolean value |

---

## Truth Tables

### AND

| A | B | Result |
|---|---|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### OR

| A | B | Result |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### NOT

| Expression | Result |
|------------|--------|
| `not True` | False |
| `not False` | True |
