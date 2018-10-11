def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def multiply(numbers):
    total = 1
    for n in numbers:
        total = total * n
    return total



print(sum([1, 2, 9, 4]))
print(multiply([1, 7, 3, 4]))