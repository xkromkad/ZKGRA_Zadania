#author: David Kromka
#Task 1
print("Task 1 \n")
def find_prime_roots_modulo(n):
    prime_roots = []
    for a in range(1, n):

        residues = []
        for x in range(1, n):
            y = (a ** x) % n
            residues.append(y)
            if len(residues) == n - 1:
                prime_roots.append(residues)
    return prime_roots

n_values = [5, 11]

for n in n_values:
    prime_roots = find_prime_roots_modulo(n)
    print(f"Prime roots modulo {n} are: {set(item for sublist in prime_roots for item in sublist)}")
    print(f"Table of reflections for n = {n}:")
    print("   x   |", end="")
    for a in range (1,len(prime_roots)+1):
        print(f" {a:3}", end="")
    print("\n" + "-" * (6 + len(prime_roots) * 4))
    for x in range(1, n):
        print(f"   {x:3} |", end="")
        print('   ' +'   '.join(str(num) for num in prime_roots[x-1]))
        print()
    print()

#Task 2
print("Task 2 \n")
def find_x(a, y):
    possible_x = []
    for x in range(0, 7):
        if (a ** x) % 7 == y:
            possible_x.append(x)
    return tuple(possible_x)

combinations = [
    (1, 1),
    (3, 4),
    (4, 2),
    (5, 6),
    (6, 6)
]

results = {}

for a, y in combinations:
    possible_x_values = find_x(a, y)
    if possible_x_values:
        results[(a, possible_x_values)] = y

# Display the results in a table
print("a  |  x    |  y")
print("-- | --   | --")
for (a, x_values), y in results.items():
    x_str = ", ".join(str(x) for x in x_values)
    print(f"{a}  |  {x_str} |  {y}")
