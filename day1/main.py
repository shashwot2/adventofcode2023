try:
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        numeric_chars = [(char) for char in line if char.isnumeric()]

        if numeric_chars:
            first = numeric_chars[0]
            last = numeric_chars[-1]
            total += int(first + last)

    print(total)

except Exception as e:
    print("Error:", e)
