# define the set S
S = [0, 1, 2]

# Print table header
print("Cayley Table (a * b = (a + b) mod 3)\n")

print("  |", end=" ")
for b in S:
    print(b, end=" ")
print()

print("--+" + "---" * len(S))

for a in S:
    print(a, "|", end=" ")
    for b in S:
        print((a + b) % 3, end=" ")
    print()
