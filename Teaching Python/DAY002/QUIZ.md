# Multiple Choice Questions (MCQs)

## Question 1

### Which line of Python code is valid?

A.

```python
var a = 12
```

B.

```python
a = 12
```

C.

```python
a: 12
```

D.

```python
12 = a
```

### Answer

✅ **B**

```python
a = 12
```

### Explanation

- ❌ `var` is used in JavaScript, not Python.
- ✅ Python variables are created simply by assigning a value.
- ❌ `a: 12` is invalid syntax.
- ❌ `12 = a` is invalid because the value cannot be on the left side of the assignment operator.

---

## Question 2

### Which is the best variable name for Player 1's username?

A.

```python
p1 user name = "jackbauer"
```

B.

```python
1_player_username = "jackbauer"
```

C.

```python
player1_username = "jackbauer"
```

D.

```python
p1u = "jackbauer"
```

### Answer

✅ **C**

```python
player1_username = "jackbauer"
```

### Explanation

- ❌ Variable names cannot contain spaces.
- ❌ Variable names cannot start with a number.
- ✅ `player1_username` is meaningful and follows Python's snake_case naming convention.
- ❌ `p1u` is valid but not descriptive.

---

## Question 3

### Which block of code will produce an error?

### Block 1

```python
time_until_midnight = "5"
print("There are " + time_until_Midnight + " hours until midnight")
```

### Block 2

```python
num_hours = "5"
print("There are " + num_hours + " hours until midnight")
```

### Block 3

```python
time_until_midnight = "5"
print("There are " + time_until_midnight + " hours until midnight")
```

### Answer

✅ **Block 1**

### Error Type

```
NameError
```

### Why?

Python is **case-sensitive**.

You created:

```python
time_until_midnight
```

but tried to use:

```python
time_until_Midnight
```

Notice the capital **M**.

Python thinks these are two different variables.

---

Block 2 ✅ Works correctly.

Block 3 ✅ Works correctly.

---

# Additional Practice MCQs

## Question 4

### Which function is used to display output on the screen?

A.

```python
display()
```

B.

```python
echo()
```

C.

```python
print()
```

D.

```python
output()
```

### Answer

✅ **C**

```python
print()
```

---

## Question 5

### Which function is used to accept user input?

A.

```python
read()
```

B.

```python
scan()
```

C.

```python
input()
```

D.

```python
accept()
```

### Answer

✅ **C**

```python
input()
```

---

## Question 6

### What is the output?

```python
name = "Sri"
print("Hello " + name)
```

A.

```
Hello
Sri
```

B.

```
HelloSri
```

C.

```
Hello Sri
```

D.

```
Sri Hello
```

### Answer

✅ **C**

```
Hello Sri
```

---

## Question 7

### What is the output?

```python
print("Hello\nWorld")
```

A.

```
Hello World
```

B.

```
Hello\nWorld
```

C.

```
Hello
World
```

D.

```
World
Hello
```

### Answer

✅ **C**

---

## Question 8

### Which of these is a valid variable name?

A.

```python
my-name
```

B.

```python
2name
```

C.

```python
my_name
```

D.

```python
my name
```

### Answer

✅ **C**

```python
my_name
```

---

## Question 9

### What does `len("Python")` return?

A.

```
5
```

B.

```
6
```

C.

```
7
```

D.

```
8
```

### Answer

✅ **B**

```
6
```

---

## Question 10

### What is the output?

```python
print("Hello" + " " + "World")
```

A.

```
HelloWorld
```

B.

```
Hello World
```

C.

```
Hello  World
```

D.

```
World Hello
```

### Answer

✅ **B**

```
Hello World
```

---

## Question 11

### Which character is used to write a comment in Python?

A.

```
//
```

B.

```
#
```

C.

```
--
```

D.

```
**
```

### Answer

✅ **B**

```
#
```

---

## Question 12

### Which operator is used to join (concatenate) two strings?

A.

```
*
```

B.

```
&
```

C.

```
+
```

D.

```
/
```

### Answer

✅ **C**

```
+
```

---

# Quick Revision

| Topic | Remember |
|--------|----------|
| Print output | `print()` |
| User input | `input()` |
| Comment | `#` |
| Find length | `len()` |
| Join strings | `+` |
| New line | `\n` |
| Variables | Use meaningful snake_case names |
| Python is | Case-sensitive |
| Valid assignment | `name = value` |
| Best naming style | `first_name`, `player1_username` |
