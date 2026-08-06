# Python Indentation Quiz

## Question 1

### Which version of code will produce an **Indentation Error** when it is run?

> **Note:** The `.` symbol represents a single space.

---

### Option A

```python
def my_function():
 .print("Hello")
```

### Option B

```python
def my_function():
print("Hello")
```

### Option C

```python
def my_function():
....print("Hello")
```

### Option D

```python
def my_function():
..print("Hello")
..print("Bye")
```

---

## Answer

✅ **Option B**

### Explanation

Python uses indentation to define a block of code.

A function body **must be indented**.

Correct examples:

```python
def my_function():
    print("Hello")
```

or

```python
def my_function():
        print("Hello")
```

Incorrect:

```python
def my_function():
print("Hello")
```

Output:

```
IndentationError: expected an indented block
```

---

# Question 2

## Which code will run successfully?

### Option A

```python
def greet():
    print("Hello")

greet()
```

### Option B

```python
def greet():
print("Hello")

greet()
```

### Option C

```python
def greet():
        print("Hello")
    print("Bye")

greet()
```

### Option D

```python
def greet()
    print("Hello")

greet()
```

---

## Answer

✅ **Option A**

### Explanation

A function:

- Requires a colon `:` after the function name.
- Requires an indented body.

Correct:

```python
def greet():
    print("Hello")
```

---

# Question 3

## In which version of code will you see `"This will run"` printed?

> **Note:** The `.` symbol represents a single space.

---

### Option A

```python
def my_function():
....a = 3
....if a > 2:
....print("This will run")

my_function()
```

---

### Option B

```python
def my_function():
a = 3
....if a > 2:
........print("This will run")

my_function()
```

---

### Option C

```python
def my_function():
....a = 3
....if a > 2:
........print("This will run")
....my_function()
```

---

### Option D

```python
def my_function():
....a = 3
....if a > 2:
........print("This will run")

my_function()
```

---

## Answer

✅ **Option D**

### Explanation

Correct indentation:

```python
def my_function():
    a = 3

    if a > 2:
        print("This will run")

my_function()
```

Execution flow:

1. Function is created.
2. `my_function()` is called.
3. `a` is assigned value `3`.
4. Condition `a > 2` is True.
5. Message is printed.

Output:

```
This will run
```

---

# Question 4

## What will be the output?

```python
def test():
    x = 10
    if x == 10:
        print("Correct")

test()
```

Options:

A. Error  
B. Correct  
C. Nothing printed  
D. None  

---

## Answer

✅ **B. Correct**

Explanation:

The condition:

```python
x == 10
```

is True, so the print statement executes.

---

# Question 5

## What error will this code produce?

```python
def test():
    print("Hello")

print("Bye")
test()
```

Options:

A. Indentation Error  
B. Syntax Error  
C. No Error  
D. Name Error  

---

## Answer

✅ **C. No Error**

Output:

```
Bye
Hello
```

Explanation:

Both statements are correctly placed.

---

# Question 6

## Which indentation is correct for a nested `if` statement?

### Option A

```python
if True:
print("Hello")
```

### Option B

```python
if True:
    print("Hello")
```

### Option C

```python
if True:
        print("Hello")
```

### Option D

```python
if True
    print("Hello")
```

---

## Answer

✅ **Option B**

Explanation:

The standard Python style uses **4 spaces** for each indentation level.

---

# Question 7

## What will this code print?

```python
def check():
    number = 5

    if number > 10:
        print("Greater")
    else:
        print("Smaller")

check()
```

Options:

A.

```
Greater
```

B.

```
Smaller
```

C. Error

D. Nothing

---

## Answer

✅ **B. Smaller**

Explanation:

`5 > 10` is False, so the `else` block runs.

---

# Question 8

## What happens when this code runs?

```python
def hello():
    print("Hello")

hello()
hello()
```

Options:

A. Prints Hello once  
B. Prints Hello twice  
C. Error  
D. Prints nothing  

---

## Answer

✅ **B. Prints Hello twice**

Output:

```
Hello
Hello
```

Explanation:

A function can be called multiple times.

---

# Question 9

## Which keyword is used to create a function in Python?

Options:

A. function  
B. create  
C. def  
D. fun  

---

## Answer

✅ **C. def**

Example:

```python
def my_function():
    print("Hello")
```

---

# Question 10

## What will happen if a function is defined but never called?

Example:

```python
def welcome():
    print("Welcome")
```

Options:

A. Welcome is printed automatically  
B. Syntax Error  
C. Nothing happens  
D. Python exits  

---

## Answer

✅ **C. Nothing happens**

Explanation:

Defining a function only stores it.

It runs only when called:

```python
welcome()
```

---

# Key Python Indentation Rules

| Rule | Example |
|---|---|
| Function body must be indented | `def test():` → `    print()` |
| `if` block must be indented | `if x:` → `    print()` |
| Nested blocks need extra indentation | `if` inside function |
| Use consistent spaces | Usually 4 spaces |
| Missing indentation causes errors | `IndentationError` |

---

# Exam Tips

✅ After `def`, `if`, `for`, `while`, `class` → expect indentation.

✅ A colon `:` starts a new code block.

✅ Function definitions do not execute automatically.

✅ Function calls execute the code.

✅ Incorrect indentation is one of the most common Python errors.
