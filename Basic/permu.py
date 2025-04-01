from itertools import permutations
def generate_even_combinations(digits):
    evens = []
    for last in [2, 4]:  # Only even endings
        remaining = [d for d in digits if d != last]
        for p in permutations(remaining, 2):
            num = int(''.join(map(str, p)) + str(last))
            evens.append(num)
    return evens

digits = [1, 2, 3, 4]
print(generate_even_combinations(digits))