# Python Dictionary – Interview & Practice Questions

A collection of Python dictionary questions ranging from basic concepts to scenario-based and interview-style questions.

---

## 1. Basic Dictionary Operations

### Question 1: Adding a New Key

Which line of code will change the `starting_dictionary` to the `final_dictionary`?

**Starting Dictionary**
```python
starting_dictionary = {
    "a": 9,
    "b": 8,
}
```

**Final Dictionary**
```python
final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
```

**Options**
- `final_dictionary = starting_dictionary.append({"c": 7})`
- `final_dictionary = starting_dictionary += {"c": 7}`
- `final_dictionary = starting_dictionary["c"]: 7`
- `final_dictionary = starting_dictionary["c"] = 7`
- `starting_dictionary["c"] = 7`

**Answer**
```python
starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
```

**Explanation**

Dictionaries allow you to add a new key by assigning a value to it.

```python
dictionary["new_key"] = value
```

---

### Question 2: Accessing a Dictionary Key

Which line of code will produce an error?

```python
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
```

**Options**
- `dict["c"] = [1, 2, 3]`
- ```python
  for key in dict:
      dict[key] += 1
  ```
- `dict[1] = 4`
- `print(dict[1])`

**Answer**
```python
print(dict[1])
```

**Explanation**

The dictionary does not contain a key `1`.

```python
dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

Therefore:
```python
dict[1]
```

causes:
```
KeyError: 1
```

Unlike a list, dictionary indexing does not mean "give me the second item."

---

### Question 3: Nested Dictionaries

Which line of code will print "Steak"?

```python
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
```

**Options**
- `print(order["main"][2])`
- `print(order["dessert" - 1][2][0])`
- `print(order[main][2][0])`
- `print(order["main"][2][0])`
- `print(order["main"][1][0])`

**Answer**
```python
print(order["main"][2][0])
```

**Explanation**

The lookup happens in three stages:

```python
order["main"]
```
returns:
```python
{1: ["Burger", "Fries"], 2: ["Steak"]}
```

Then:
```python
order["main"][2]
```
returns:
```python
["Steak"]
```

Finally:
```python
order["main"][2][0]
```
returns:
```
Steak
```

---

## 2. Creating and Updating Dictionaries

### Question 4: Create an Empty Dictionary

Which statement creates an empty dictionary?

**Options**
- `dict = []`
- `dict = {}`
- `dict = ()`
- `dict = ""`

**Answer**
```python
dict = {}
```

**Explanation**

`{}` creates an empty dictionary.

---

### Question 5: Add Multiple Values

What will this code print?

```python
student = {}

student["name"] = "John"
student["age"] = 25

print(student)
```

**Answer**
```
{'name': 'John', 'age': 25}
```

---

### Question 6: Updating an Existing Key

What will this code print?

```python
person = {
    "name": "John",
    "age": 25
}

person["age"] = 30

print(person)
```

**Answer**
```
{'name': 'John', 'age': 30}
```

**Explanation**

Assigning a value to an existing key updates that key.

---

### Question 7: Duplicate Keys

What will this code print?

```python
data = {
    "name": "John",
    "name": "David"
}

print(data)
```

**Answer**
```
{'name': 'David'}
```

**Explanation**

Dictionary keys must be unique.

If the same key appears more than once, the last value replaces the previous value.

---

### Question 8: Dictionary Length

What will this print?

```python
data = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(len(data))
```

**Answer**
```
3
```

**Explanation**

`len()` returns the number of key-value pairs.

---

## 3. Accessing Dictionary Values

### Question 9: Accessing a Value

What will this print?

```python
person = {
    "name": "John",
    "age": 30
}

print(person["name"])
```

**Answer**
```
John
```

---

### Question 10: Missing Key

What happens here?

```python
person = {
    "name": "John"
}

print(person["age"])
```

**Answer**

It produces:
```
KeyError: 'age'
```

---

### Question 11: Using get()

What will this print?

```python
person = {
    "name": "John"
}

print(person.get("age"))
```

**Answer**
```
None
```

**Explanation**

Unlike:
```python
person["age"]
```

`get()` does not raise a `KeyError` when the key does not exist.

---

### Question 12: get() with Default Value

What will this print?

```python
person = {
    "name": "John"
}

print(person.get("age", 0))
```

**Answer**
```
0
```

---

### Question 13: Check Whether a Key Exists

Which statement checks whether `"name"` exists?

```python
person = {
    "name": "John",
    "age": 30
}
```

**Options**
- `if "name" in person`
- `if person contains "name"`
- `if person.has("name")`
- `if person.key("name")`

**Answer**
```python
if "name" in person:
    print("Found")
```

---

## 4. Dictionary Keys and Values

### Question 14: Get All Keys

Which method returns all dictionary keys?

**Options**
- `dict.keys()`
- `dict.values()`
- `dict.items()`
- `dict.all()`

**Answer**
```python
dict.keys()
```

---

### Question 15: Get All Values

Which method returns all values?

**Answer**
```python
dict.values()
```

Example:
```python
data = {
    "a": 10,
    "b": 20
}

print(data.values())
```

---

### Question 16: Get Key-Value Pairs

Which method returns key-value pairs?

**Answer**
```python
dict.items()
```

Example:
```python
data = {
    "a": 10,
    "b": 20
}

for key, value in data.items():
    print(key, value)
```

Output:
```
a 10
b 20
```

---

### Question 17: Loop Through Keys

What does this print?

```python
data = {
    "a": 1,
    "b": 2
}

for key in data:
    print(key)
```

**Answer**
```
a
b
```

**Explanation**

Iterating directly over a dictionary iterates over its keys.

---

### Question 18: Loop Through Values

Which code prints the values?

**Answer**
```python
for value in data.values():
    print(value)
```

---

### Question 19: Loop Through Keys and Values

Which code is correct?

**Answer**
```python
for key, value in data.items():
    print(key, value)
```

---

## 5. Removing Dictionary Entries

### Question 20: Remove a Key

Which method removes a key?

**Options**
- `remove()`
- `delete()`
- `pop()`
- `erase()`

**Answer**
```python
dict.pop(key)
```

Example:
```python
data = {
    "a": 1,
    "b": 2
}

data.pop("a")

print(data)
```

Output:
```
{'b': 2}
```

---

### Question 21: Using del

What will this do?

```python
data = {
    "a": 1,
    "b": 2
}

del data["a"]
```

**Answer**

It removes key `"a"`.

The resulting dictionary is:
```
{'b': 2}
```

---

### Question 22: Remove Everything

Which method removes all entries from a dictionary?

**Answer**
```python
dict.clear()
```

Example:
```python
data = {
    "a": 1,
    "b": 2
}

data.clear()

print(data)
```

Output:
```
{}
```

---

### Question 23: pop() Return Value

What will this print?

```python
data = {
    "a": 10,
    "b": 20
}

x = data.pop("a")

print(x)
```

**Answer**
```
10
```

`pop()` removes the key and returns its value.

---

## 6. Copying Dictionaries

### Question 24: Dictionary Assignment

What happens here?

```python
a = {
    "x": 10
}

b = a

b["x"] = 20

print(a)
```

**Answer**
```
{'x': 20}
```

**Explanation**

`b = a` does not create an independent copy.

Both variables refer to the same dictionary.

---

### Question 25: Copy a Dictionary

Which method creates a shallow copy?

**Options**
- `dict.copy()`
- `dict.clone()`
- `dict.duplicate()`
- `dict.new()`

**Answer**
```python
new_dict = old_dict.copy()
```

---

### Question 26: Copy Example

What will this print?

```python
a = {
    "x": 10
}

b = a.copy()

b["x"] = 20

print(a)
print(b)
```

**Answer**
```
{'x': 10}
{'x': 20}
```

---

## 7. Nested Dictionaries

### Question 27: Access Nested Data

What will this print?

```python
users = {
    "user1": {
        "name": "John",
        "age": 30
    }
}

print(users["user1"]["name"])
```

**Answer**
```
John
```

---

### Question 28: Update Nested Data

Change John's age to 31.

```python
users = {
    "user1": {
        "name": "John",
        "age": 30
    }
}
```

**Answer**
```python
users["user1"]["age"] = 31
```

---

### Question 29: Nested Dictionary Loop

What will this print?

```python
users = {
    "user1": {"name": "John"},
    "user2": {"name": "David"}
}

for user, details in users.items():
    print(user, details["name"])
```

**Answer**
```
user1 John
user2 David
```

---

## 8. Dictionaries Containing Lists

### Question 30: Access a List Inside a Dictionary

What will this print?

```python
data = {
    "servers": ["server1", "server2", "server3"]
}

print(data["servers"][1])
```

**Answer**
```
server2
```

---

### Question 31: Add to a List Inside a Dictionary

How do you add `"server4"`?

```python
data = {
    "servers": ["server1", "server2"]
}
```

**Answer**
```python
data["servers"].append("server4")
```

Result:
```python
{
    "servers": ["server1", "server2", "server4"]
}
```

---

### Question 32: Dictionary with List of Dictionaries

What will this print?

```python
servers = {
    "production": [
        {"name": "server1", "ip": "10.0.0.1"},
        {"name": "server2", "ip": "10.0.0.2"}
    ]
}

print(servers["production"][1]["ip"])
```

**Answer**
```
10.0.0.2
```

---

## 9. Dictionary Methods

### Question 33: setdefault()

What will this print?

```python
data = {
    "name": "John"
}

data.setdefault("age", 30)

print(data)
```

**Answer**
```
{'name': 'John', 'age': 30}
```

**Explanation**

`setdefault()` adds the key only if it does not already exist.

---

### Question 34: setdefault() Existing Key

What will this print?

```python
data = {
    "age": 25
}

data.setdefault("age", 30)

print(data)
```

**Answer**
```
{'age': 25}
```

The existing value is not replaced.

---

### Question 35: update()

What will this print?

```python
data = {
    "a": 1,
    "b": 2
}

data.update({"b": 20, "c": 30})

print(data)
```

**Answer**
```
{'a': 1, 'b': 20, 'c': 30}
```

**Explanation**

`update()`:
- modifies existing keys
- adds new keys

---

### Question 36: Merge Dictionaries

What will this print?

```python
a = {
    "x": 1,
    "y": 2
}

b = {
    "y": 20,
    "z": 3
}

c = a | b

print(c)
```

**Answer**
```
{'x': 1, 'y': 20, 'z': 3}
```

**Explanation**

The `|` operator merges dictionaries.

If the same key exists in both dictionaries, the value from the right-hand dictionary wins.

---

## 10. Dictionary Comprehension

### Question 37: Basic Dictionary Comprehension

What will this produce?

```python
numbers = [1, 2, 3, 4]

result = {x: x * 2 for x in numbers}

print(result)
```

**Answer**
```
{1: 2, 2: 4, 3: 6, 4: 8}
```

---

### Question 38: Dictionary Comprehension with Condition

Create a dictionary containing only even numbers.

```python
numbers = [1, 2, 3, 4, 5, 6]
```

**Answer**
```python
result = {
    x: x * 2
    for x in numbers
    if x % 2 == 0
}
```

Result:
```python
{
    2: 4,
    4: 8,
    6: 12
}
```

---

### Question 39: Convert List to Dictionary

What will this produce?

```python
numbers = [1, 2, 3]

result = {x: x ** 2 for x in numbers}

print(result)
```

**Answer**
```
{1: 1, 2: 4, 3: 9}
```

---

## 11. Dictionary Keys

### Question 40: Can a List Be a Dictionary Key?

Will this work?

```python
data = {
    [1, 2]: "value"
}
```

**Answer**

No.

It produces:
```
TypeError: unhashable type: 'list'
```

**Explanation**

Dictionary keys must be hashable.

Lists are mutable and therefore cannot be dictionary keys.

---

### Question 41: Can a Tuple Be a Key?

Will this work?

```python
data = {
    (1, 2): "value"
}
```

**Answer**

Yes.

Tuples can be dictionary keys if their contents are hashable.

---

### Question 42: Can an Integer Be a Key?

Will this work?

```python
data = {
    1: "one",
    2: "two"
}
```

**Answer**

Yes.

Dictionary keys can be integers.

---

### Question 43: Can Different Data Types Be Keys?

Will this work?

```python
data = {
    "name": "John",
    1: "one",
    (1, 2): "tuple"
}
```

**Answer**

Yes.

A dictionary can contain keys of different hashable types.

---

## 12. Scenario-Based Questions

### Question 44: Count Occurrences

Write Python code to count how many times each item occurs.

```python
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
```

**Answer**
```python
counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1

print(counts)
```

Output:
```
{'apple': 3, 'banana': 2, 'orange': 1}
```

---

### Question 45: Find the Highest Value

Find the employee with the highest salary.

```python
employees = {
    "John": 50000,
    "David": 65000,
    "Sarah": 55000
}
```

**Answer**
```python
highest = max(employees, key=employees.get)

print(highest)
```

Output:
```
David
```

---

### Question 46: Find the Highest Salary

How do you get the highest salary itself?

```python
employees = {
    "John": 50000,
    "David": 65000,
    "Sarah": 55000
}
```

**Answer**
```python
highest_salary = max(employees.values())

print(highest_salary)
```

Output:
```
65000
```

---

### Question 47: Check for Duplicate Values

Which statement is true?

```python
data = {
    "a": 10,
    "b": 20,
    "c": 10
}
```

**Answer**

Duplicate values are allowed.

Here:
```
a -> 10
c -> 10
```

Both keys can have the same value.

However, duplicate keys are not allowed.

---

### Question 48: Reverse a Dictionary

Given:
```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

Create:
```python
{
    1: "a",
    2: "b",
    3: "c"
}
```

**Answer**
```python
result = {
    value: key
    for key, value in data.items()
}
```

---

### Question 49: Merge Two Dictionaries

Given:
```python
linux = {
    "server1": "RHEL",
    "server2": "Ubuntu"
}

unix = {
    "server3": "Solaris",
    "server4": "AIX"
}
```

Create one dictionary containing all servers.

**Answer**
```python
servers = linux.copy()
servers.update(unix)

print(servers)
```

Result:
```python
{
    "server1": "RHEL",
    "server2": "Ubuntu",
    "server3": "Solaris",
    "server4": "AIX"
}
```

---

### Question 50: Infrastructure Scenario

You have server information:

```python
servers = {
    "server01": {
        "os": "RHEL",
        "environment": "prod",
        "status": "running"
    },
    "server02": {
        "os": "Ubuntu",
        "environment": "dev",
        "status": "stopped"
    },
    "server03": {
        "os": "RHEL",
        "environment": "prod",
        "status": "running"
    }
}
```

Write code to print the names of all production servers.

**Answer**
```python
for server, details in servers.items():
    if details["environment"] == "prod":
        print(server)
```

Output:
```
server01
server03
```

---

## Quick Dictionary Cheat Sheet

| Operation | Syntax |
|---|---|
| Create dictionary | `d = {}` |
| Add key | `d["key"] = value` |
| Update key | `d["key"] = new_value` |
| Access value | `d["key"]` |
| Safe access | `d.get("key")` |
| Check key | `"key" in d` |
| Get keys | `d.keys()` |
| Get values | `d.values()` |
| Get pairs | `d.items()` |
| Remove key | `d.pop("key")` |
| Delete key | `del d["key"]` |
| Remove all | `d.clear()` |
| Copy | `d.copy()` |
| Update/merge | `d.update(other)` |
| Dictionary length | `len(d)` |
| Loop keys | `for key in d:` |
| Loop values | `for value in d.values():` |
| Loop pairs | `for k, v in d.items():` |

---

## Important Interview Points

### 1. Dictionary vs List

A list uses positional indexes:
```python
items = ["a", "b", "c"]

print(items[1])
```
Output:
```
b
```

A dictionary uses keys:
```python
items = {
    "first": "a",
    "second": "b"
}

print(items["second"])
```
Output:
```
b
```

### 2. Dictionary Keys Must Be Unique

```python
data = {
    "a": 1,
    "a": 2
}
```
Result:
```python
{"a": 2}
```

### 3. Dictionary Values Can Be Duplicated

```python
data = {
    "a": 10,
    "b": 10
}
```
This is completely valid.

### 4. Missing Key

This raises an exception:
```python
data["missing"]
```

Use this when you want a safe lookup:
```python
data.get("missing")
```

### 5. Dictionary Lookup

Average dictionary lookup is:
```
O(1)
```
because Python dictionaries use a hash table internally.

---

## Interview Revision

Remember these five patterns:

**Add**
```python
d["key"] = value
```

**Read**
```python
value = d["key"]
```

**Safe Read**
```python
value = d.get("key")
```

**Delete**
```python
d.pop("key")
```

**Iterate**
```python
for key, value in d.items():
    print(key, value)
```

These are among the most commonly tested Python dictionary operations.
