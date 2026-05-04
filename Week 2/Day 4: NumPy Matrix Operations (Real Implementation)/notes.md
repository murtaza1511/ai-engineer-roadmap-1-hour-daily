## 🎯 Today’s Goal (1 Hour)

By the end of today:

```text
You should be able to:
→ represent matrices using NumPy
→ perform matrix multiplication instantly
→ think in terms of vectorized operations (not loops)
```

---

# 🧠 Part 1 — Why NumPy Exists (10 min)

So far you did:

```python
for row in W:
    for i in range(len(x)):
        ...
```

That’s good for learning — but **not scalable**.

---

## 🔥 Problem

* Slow
* Verbose
* Not how real ML systems work

---

## 💡 Solution → NumPy

NumPy

```text
NumPy = fast numerical computation engine for Python
```

Used in:

* machine learning
* deep learning
* data science
* scientific computing

---

## 🧠 Core Idea

```text
List → basic storage  
NumPy array → mathematical object
```

---

# 💻 Part 2 — Getting Started (15 min)

## Step 1 — Install (if not already)

```bash
pip install numpy
```

---

## Step 2 — Create Arrays

```python
import numpy as np

# vector
x = np.array([5, 6])

# matrix
W = np.array([
    [1, 2],
    [3, 4]
])

print(x)
print(W)
```

---

## 🧠 Important Difference

```text
Python list ≠ NumPy array
```

NumPy arrays support:

* math operations
* matrix multiplication
* broadcasting (later)

---

# ⚡ Part 3 — Matrix Multiplication (Core) (15 min)

Yesterday you did manual loops.

Now:

```python
y = np.dot(W, x)

print(y)
```

---

## 🧠 What just happened?

```text
np.dot(W, x) = matrix multiplication
```

Same as:

```text
y = W · x
```

---

## 🔥 Reconnect to Concept

$$
y = Wx
$$

---

## 💡 Insight

```text
Neural networks = many np.dot() operations
```

---

# 🧪 Part 4 — Experiment Like Engineer (15–20 min)

Don’t just run — **play with it**.

---

## Experiment 1 — Change Input

```python
x = np.array([10, 20])
y = np.dot(W, x)
print(y)
```

---

## Experiment 2 — Change Weights

```python
W = np.array([
    [0.5, 1.0],
    [1.5, 0.2]
])
```

---

## Observe

```text
How output changes when:
→ input changes
→ weights change
```

---

## 🧠 Key Realization

```text
Weights define behavior of the system
```

---

# 🧠 Part 5 — Shape in NumPy (CRITICAL)

```python
print(W.shape)
print(x.shape)
```

---

## Example Output

```text
(2, 2)
(2,)
```

---

## 🧠 Meaning

```text
(2, 2) → 2 rows, 2 columns  
(2,)   → vector of size 2
```

---

## ⚠️ Try This (Important)

Break it intentionally:

```python
x = np.array([5, 6, 7])
np.dot(W, x)
```

👉 See the error.

---

## 💡 Insight

```text
Shape mismatch = most common ML bug
```

---

# 🧪 Part 6 — Mini Project (15–20 min)

## Build: 2-Layer Transformation System

---

### Step 1

```python
import numpy as np

W1 = np.array([
    [1, 2],
    [3, 4]
])

W2 = np.array([
    [2, 0],
    [1, 2]
])

x = np.array([5, 6])
```

---

### Step 2 — Layer 1

```python
h = np.dot(W1, x)
```

---

### Step 3 — Layer 2

```python
y = np.dot(W2, h)

print("Output:", y)
```

---

## 🧠 What You Just Built

```text
x → W1 → hidden → W2 → output
```

👉 This is a **neural network (without activation yet)**

---

# ⚠️ Common Mistakes

Avoid:

❌ Going back to loops
❌ Ignoring `.shape`
❌ Treating NumPy like lists

---

# 🧠 Reflection (Must Answer)

1. Why is NumPy faster than loops?
2. What does `np.dot()` actually do?
3. What happens when shapes don’t match?
4. Why is this operation used in every neural network?

---

# 📚 Resources (Minimal + High Value)

### 🎥 YouTube

Search:

👉 **"NumPy tutorial for beginners (core concepts only)"**

---

### 💡 Optional

Search:

👉 **"Vectorization in NumPy explained"**

---

# 🧭 Mentor Insight

This is a subtle but important shift:

Before:

```text
You were simulating math
```

Now:

```text
You are using real computational tools
```

---

# ✅ Completion Criteria

You are DONE if:

* You can create arrays using NumPy
* You can perform `np.dot()`
* You understand `.shape`
* You can build 2-layer transformation