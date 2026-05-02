W = [
    [0.5, 1.0],
    [1.5, 0.2]
]

x = [10, 20]

y = []

for row in W:
    value = 0
    for i in range(len(x)):
        value += row[i] * x[i]
    y.append(value)

print(y)