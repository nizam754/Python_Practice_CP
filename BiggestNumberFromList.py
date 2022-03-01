# Let's get max number from a list

invoices = [6, 10, 20, 47, 69, 11, 50, 230, 20, 24, 39, 29, -45]

def biggest(numbers):
    biggest_number = numbers[0]
    for number in numbers:
        if number > biggest_number:
            biggest_number = number
    return biggest_number

print(biggest(invoices))
