# Python Basics - Day 2 Exercises

## 1) Printing Practice

### Question
Write a program that prints the following recipe exactly as shown.

### Expected Output

```
1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.
```

### Solution

```python
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
```

---

# 2) Print "Hello World!" 3 Times Using Only One print()

### Question

Print **Hello World!** three times on three separate lines using only one `print()` statement.

### Solution

Use the newline character `\n`.

```python
print("Hello World!\nHello World!\nHello World!")
```

### Output

```
Hello World!
Hello World!
Hello World!
```

---

# 3) String Concatenation

### Code

```python
print("Hello" " " + "Sri")
```

### Output

```
Hello Sri
```

### Explanation

Python automatically joins adjacent strings.

```python
"Hello" " "
```

becomes

```python
"Hello "
```

which is then concatenated with `"Sri"`.

---

# 4) Fix the Indentation Error

### Incorrect Code

```python
print("Hello World\n Hello World")
 print("Hello" " " + "Sri")
```

### Error

```
IndentationError: unexpected indent
```

### Why?

The second line starts with an extra space.

Python thinks you're starting a code block, but no block exists.

### Solution

```python
print("Hello World\n Hello World")
print("Hello" " " + "Sri")
```

### Output

```
Hello World
 Hello World
Hello Sri
```

---

# 5) Fix the Syntax Error

### Incorrect Code

```python
print("Hello World\n Hello World)"
print("Hello" " " + "Sri")
```

### Error

```
SyntaxError: '(' was never closed
```

### Why?

The closing double quote is missing.

### Solution

```python
print("Hello World\n Hello World")
print("Hello" " " + "Sri")
```

---

# 6) Fix the Following Code

### Incorrect Code

```python
print(Notes from Day 1")
 print("The print statement is used to output strings")
print("Strings are strings of characters"
priint("String Concatenation is done with the + sign")
print(("New lines can be created with a \ and the letter n")
```

### Errors

- Missing opening quote
- Extra indentation
- Missing closing bracket
- `priint` is misspelled
- Extra `(`
- Escape character not escaped

### Solution

```python
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \\ and the letter n")
```

### Output

```
Notes from Day 1
The print statement is used to output strings
Strings are strings of characters
String Concatenation is done with the + sign
New lines can be created with a \ and the letter n
```

---

# 7) Input Function

## 7.1 Taking User Input

```python
input("What's your name? ")
```

### Output

```
What's your name? Sri
```

---

## 7.2 Printing the Name

```python
print("Hello" + input("What's your name? "))
```

### Output

```
What's your name? Sri
HelloSri
```

### Question

How do you add a space after **Hello**?

### Solution

```python
print("Hello " + input("What's your name? "))
```

### Output

```
What's your name? Sri
Hello Sri
```

---

## 7.3 Add an Exclamation Mark

### Required Output

```
Hello Sri!
```

### Solution

```python
print("Hello " + input("What's your name? ") + "!")
```

### Output

```
What's your name? Sri
Hello Sri!
```

---

# 8) Comments

Comments are ignored by Python and are used to explain code.

Use the `#` symbol.

```python
# This is a comment

print("Hello World")
```

Comments make your code easier to understand.

---

# 9) Variables

Variables are used to store data.

### Example

```python
name = input("Enter your name: ")
print(name)
```

### Output

```
Enter your name: Sri
Sri
```

---

## 9.2 Reassigning Variables

```python
name = input("Enter your name: ")
print(name)

name = "Sriram"
print(name)
```

### Output

```
Enter your name: Sri
Sri
Sriram
```

### Explanation

The value stored in `name` changes from the user input to `"Sriram"`.

---

## Finding the Length of a Variable

```python
name = input("Enter your name: ")
print(len(name))
```

### Output

```
Enter your name: Sriram
7
```

---

## Finding Length Directly

```python
print(len(input("Enter your name: ")))
```

### Output

```
Enter your name: Krishna
7
```

---

## Store Length in Another Variable

### Question

Create a program that:

- Takes the user's name.
- Stores it in a variable called `name`.
- Finds its length.
- Stores the length in a variable called `length`.
- Prints the length.

### Solution

```python
name = input("Enter your name: ")
length = len(name)
print(length)
```

### Example Output

```
Enter your name: Sriram
7
```

---

# Summary

You learned:

- ✔ `print()`
- ✔ Newline (`\n`)
- ✔ String Concatenation (`+`)
- ✔ Syntax Errors
- ✔ Indentation Errors
- ✔ `input()`
- ✔ Comments (`#`)
- ✔ Variables
- ✔ `len()` Function
- ✔ Storing values in variables
