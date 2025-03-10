import random
# Generate 2000 random numbers between 1 and 100
random_numbers_2000 = [str(random.randint(1, 100)) for _ in range(2000)]

# Format them as a space-separated string
random_numbers_2000_string = " ".join(random_numbers_2000)
print(random_numbers_2000_string)