# Sum of Numbers

bank_numbers = [6, 10, 20, 47, 69, 11, 50, 230, 20, 24, 39, 29]

def count_numbers(numbers):
    count = 0
    for number in numbers:
        count = count + number
    return count
print(count_numbers(bank_numbers))
