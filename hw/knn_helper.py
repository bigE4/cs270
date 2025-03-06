new_point = [0.5, 0.2]

data = {
    'one': [0.3, 0.8, "A"],
    'two': [-0.3, 1.6, "B"],
    'three': [0.9, 0, "B"],
    'four': [1, 1, "A"]
}



for key, value in data.items():
    print(key)
    print(value)
    # calc manhattan distance
    mhDistance = abs(value[0] - new_point[0]) + abs(value[1] - new_point[1])
    value.append(round(mhDistance, 3))
    data[key] = value

print("3-nn are one, three, and four")
for key, value in data.items():
    print(key)
    print(value)

data2 = {
    'one': [0.3, 0.8, "A", 0.8],
    'three': [0.9, 0, "B", 0.6],
    'four': [1, 1, "A", 1.3]
}

data3 = {
    'A': [0, 0],
    'B': [0, 0]
}

weights = []

for key, value in data2.items():
    data3[value[2]][0] += value[3]
    weight = round((1 / (value[3] * value[3])), 3)
    value.append(weight)
    weights.append(weight)
    data2[key] = value
    data3[value[2]][1] += value[4]

for key, value in data3.items():
    print(key)
    print(value)
print("Output class non-weighted - 'A'")
print("Output class     weighted - 'B'")

for key, value in data2.items():
    print(key)
    print(value)

print("Regression")
regression_labels = [.6, .8, 1.2]
print(regression_labels)
print(weights)

labels_mean = round((.6 + .8 + 1.2)/3, 3)
print(labels_mean)

weighted_mean = 0
for a, b in zip(regression_labels, weights):
    weighted_mean += a*b
weighted_mean = round(weighted_mean/sum(weights), 3)
print(weighted_mean)