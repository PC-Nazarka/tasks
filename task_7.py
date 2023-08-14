numbers = list(range(0, 1000))
not_primary = set()
valid_numbers = []

for i in range(len(numbers)):
    if numbers[i] in (0, 1):
        continue
    else:
        for j in range(i + 1, len(numbers)):
            if numbers[j] % numbers[i] == 0:
                not_primary.add(numbers[j])

for i in range(len(numbers)):
    if numbers[i] not in not_primary:
        valid_numbers.append(numbers[i])

print(valid_numbers)