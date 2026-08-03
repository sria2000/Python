# Installing Python Development Environment (Windows)

## Step 1: Download and Install PyCharm
- Download **PyCharm Community Edition** from:
  - https://www.jetbrains.com/pycharm/download/
- Install using the default options.
- Ensure PyCharm is added to your system **PATH** if prompted during installation.

---

## Step 2: Install Antigravity
Open Command Prompt and run:

```cmd
pip install antigravity
```

> **Note:** If the package is unavailable, update pip first:

```cmd
python -m pip install --upgrade pip
```

---

## Step 3: Install Visual Studio Code
Download and install VS Code from:

https://code.visualstudio.com/

During installation, select:
- ✅ Add "Open with Code" action
- ✅ Add to PATH
- ✅ Register Code as an editor

Install the **Python** extension after opening VS Code.

---

## Step 4: Install Python

Download the latest version from:

https://www.python.org/downloads/

During installation:

- ✅ Check **Add Python to PATH**
- Select **Install Now**

---

## Step 5: Verify the Installation

Open Command Prompt and run:

```cmd
python --version
```

Example output:

```cmd
C:\Users\sria2>python --version
Python 3.14.5
```

You can also verify pip:

```cmd
pip --version
```

---

## Optional Checks

Check Python location:

```cmd
where python
```

Start the Python interpreter:

```cmd
python
```

Exit the interpreter:

```python
exit()
```

or press:

```text
Ctrl + Z
Enter
```

---

## Summary

1. Install PyCharm.
2. Add PyCharm to PATH.
3. Install Antigravity.
4. Install Visual Studio Code.
5. Install Python from https://www.python.org/downloads/.
6. Verify with:

```cmd
python --version
```

Expected:

```cmd
Python 3.14.5
```
