# Calling a Python Module (`my_module`)

## Program

```python
# Calling a module named my_module

import my_module

print(my_module.my_number)
```

---

## Example Module (`my_module.py`)

```python
# my_module.py

my_number = 100
```

---

## Output

```
100
```

---

# What is a Module?

A **module** is simply a **Python file (`.py`) that contains code** such as:

- Variables
- Functions
- Classes
- Constants

Modules help organize code and allow it to be reused in multiple programs.

For example:

```
my_module.py
```

is a Python module because it is a Python file.

---

## How It Works

### Step 1 - Create a module

File: `my_module.py`

```python
my_number = 100
```

---

### Step 2 - Import the module

```python
import my_module
```

Python loads the file `my_module.py`.

---

### Step 3 - Access the variable

```python
print(my_module.my_number)
```

Output

```
100
```

Notice the syntax:

```python
module_name.variable_name
```

---

# Folder Structure

```
Project/
│
├── main.py
└── my_module.py
```

`main.py`

```python
import my_module

print(my_module.my_number)
```

`my_module.py`

```python
my_number = 100
```

---

# Syntax

Import an entire module

```python
import module_name
```

Access members

```python
module_name.variable
module_name.function()
module_name.class_name()
```

---

# Another Example

`math_module.py`

```python
pi = 3.14159
```

`main.py`

```python
import math_module

print(math_module.pi)
```

Output

```
3.14159
```

---

# Why Use Modules?

Modules help to:

- Reuse code
- Organize large programs
- Avoid writing the same code repeatedly
- Share code between multiple projects
- Improve readability and maintenance

---

# Types of Modules

## 1. Built-in Modules

Already provided by Python.

Examples:

```python
import math
import random
import os
import sys
```

---

## 2. User-defined Modules

Modules created by you.

Example:

```
my_module.py
```

---

# Interview Questions

### Q1. What is a module?

**Answer:**  
A module is a Python file (`.py`) containing variables, functions, classes, or executable code that can be imported and reused.

---

### Q2. How do you import a module?

```python
import my_module
```

---

### Q3. How do you access a variable inside a module?

```python
my_module.my_number
```

---

### Q4. Why are modules used?

- Code reusability
- Better organization
- Easier maintenance
- Reduced duplication

---

# Key Points

- A **module** is a Python file (`.py`).
- Import a module using `import module_name`.
- Access variables and functions using the dot (`.`) operator.
- Modules make programs modular, reusable, and easier to maintain.
- Python provides both **built-in** and **user-defined** modules.
