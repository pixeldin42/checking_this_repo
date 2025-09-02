import random

def generate_numbers():
    actual_charge = round(random.uniform(614, 630), 2)
    p = round(random.uniform(-40, 40), 2)
    r = round(random.uniform(-0.28, 0.76), 2)
    subtotal = actual_charge
    total = round(actual_charge - p - r, 2)
    return actual_charge, p, r, subtotal, total

def print_set(number_set):
    print("Actual Charge:", number_set[0])
    print("P:", number_set[1])
    print("R:", number_set[2])
    print("Subtotal:", number_set[3])
    print("Total:", number_set[4])
    print()

# Generate and print 10 sets of numbers
for _ in range(10):
    numbers = generate_numbers()
    print_set(numbers)