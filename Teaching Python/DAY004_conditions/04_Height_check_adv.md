# Python Program - Roller Coaster Ticket Price Calculator

This program checks:

1. Whether a person is tall enough to ride the roller coaster.
2. If they are tall enough, it asks for their age.
3. Based on their age, it calculates the ticket price.

---

# Ticket Pricing

| Age | Ticket Price |
|------|-------------:|
| 18 years and above | £15 |
| 12 to 17 years | £10 |
| Below 12 years | £5 |

> **Note:** Riders must be at least **120 cm** tall to enter the ride.

---

# Python Program

```python
# Enter the height of the person.
# If height is 120 cm or more, they can ride.
# Then check their age and calculate the ticket price.

height = float(input("What's your height (in cm)? "))

if height >= 120:
    print("🎉 Yaay!! You can ride the game.")

    age = int(input("What is your age? "))

    if age >= 18:
        print("You need to pay £15 to ride the game.")
    elif age >= 12 and age < 18:
        print("You need to pay £10 to ride the game.")
    else:
        print("You need to pay £5 to ride the game.")

else:
    short_by = int(120 - height)
    print(f"Oops! You are short by {short_by} cm. Come back next year!")
```

---

# Sample Run 1

### Input

```text
What's your height (in cm)? 130
What is your age? 22
```

### Output

```text
🎉 Yaay!! You can ride the game.
You need to pay £15 to ride the game.
```

---

# Sample Run 2

### Input

```text
What's your height (in cm)? 125
What is your age? 15
```

### Output

```text
🎉 Yaay!! You can ride the game.
You need to pay £10 to ride the game.
```

---

# Sample Run 3

### Input

```text
What's your height (in cm)? 125
What is your age? 8
```

### Output

```text
🎉 Yaay!! You can ride the game.
You need to pay £5 to ride the game.
```

---

# Sample Run 4

### Input

```text
What's your height (in cm)? 110
```

### Output

```text
Oops! You are short by 10 cm. Come back next year!
```

---

# How the Program Works

## Step 1 - Read the Height

```python
height = float(input("What's your height (in cm)? "))
```

The user's height is converted to a floating-point number.

---

## Step 2 - Check the Height Requirement

```python
if height >= 120:
```

If the height is **120 cm or more**, the user is allowed to continue.

Otherwise, the program calculates how many centimetres they are short.

---

## Step 3 - Read the Age

```python
age = int(input("What is your age? "))
```

The age is converted into an integer.

---

## Step 4 - Determine the Ticket Price

### Adults (18 and above)

```python
if age >= 18:
```

Output

```text
You need to pay £15 to ride the game.
```

---

### Teenagers (12–17)

```python
elif age >= 12 and age < 18:
```

Output

```text
You need to pay £10 to ride the game.
```

The `and` operator ensures **both** conditions are true:

- Age is at least 12.
- Age is less than 18.

---

### Children (Below 12)

```python
else:
```

Output

```text
You need to pay £5 to ride the game.
```

---

## Step 5 - If the Rider Is Too Short

```python
short_by = int(120 - height)
```

Example

```
Height = 114

120 - 114

= 6
```

Display

```python
print(f"Oops! You are short by {short_by} cm. Come back next year!")
```

---

# Decision Flow

```text
                Start
                  │
                  ▼
          Enter Height
                  │
                  ▼
        Is Height ≥ 120?
          ┌──────────────┐
          │              │
         Yes             No
          │              │
          ▼              ▼
      Enter Age     Calculate
          │         Short By
          ▼              │
    Age ≥ 18 ?           ▼
     ┌─────────┐     Display
     │         │     Message
    Yes       No
     │         │
     ▼         ▼
 Pay £15   Age ≥ 12?
             ┌───────┐
             │       │
            Yes      No
             │       │
             ▼       ▼
         Pay £10   Pay £5
```

---

# Why Use `elif`?

Without `elif`, Python would check every `if` statement separately.

Using `elif` means:

- As soon as one condition is **True**, Python skips the remaining conditions.

This makes the program more efficient and easier to read.

---

# Tips for Beginners

- `>=` means **greater than or equal to**.
- `and` requires **both** conditions to be **True**.
- `elif` is short for **else if**.
- Always use indentation (4 spaces) after `if`, `elif`, and `else`.
- Use `float()` for values that may contain decimals.
- Use `int()` for whole numbers such as age.
- Use **f-strings** to insert variables into messages.

---

# Common Beginner Mistakes

### ❌ Using `=` Instead of `==`

Incorrect

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

### ❌ Forgetting `elif`

Incorrect

```python
if age >= 18:
    print("£15")

if age >= 12:
    print("£10")
```

A 20-year-old would see **both** messages.

Correct

```python
if age >= 18:
    print("£15")
elif age >= 12:
    print("£10")
```

---

### ❌ Forgetting Indentation

Incorrect

```python
if height >= 120:
print("You can ride")
```

Correct

```python
if height >= 120:
    print("You can ride")
```

---

# Quick Revision

```python
height = float(input())

if height >= 120:
    age = int(input())

    if age >= 18:
        print("£15")
    elif age >= 12:
        print("£10")
    else:
        print("£5")
else:
    print("Too short")
```

---

# Key Concepts Learned

- `input()`
- `float()`
- `int()`
- Variables
- `if`
- `elif`
- `else`
- Nested `if` statements
- Comparison operators (`>=`, `<`)
- Logical operator (`and`)
- Arithmetic operations
- f-strings
- Indentation

---

# Summary

This program combines multiple Python concepts:

- Accepting user input.
- Making decisions with `if`, `elif`, and `else`.
- Using nested conditional statements.
- Using the `and` logical operator.
- Performing simple calculations.
- Displaying user-friendly output using f-strings.
