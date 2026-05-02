# Step 1: Store degrees of vertices in a dictionary
degrees = {
    'A': 2,
    'B': 2,
    'C': 3,
    'D': 1
}

# Step 2: Display all degrees
print("Degrees of vertices:")
for vertex in degrees:
    print(f"deg({vertex}) = {degrees[vertex]}")

# Step 3: Calculate sum of all degrees
sum_of_degrees = sum(degrees.values())
print("\nSum of all degrees =", sum_of_degrees)

# Step 4: Calculate number of edges using formula
# Number of edges = sum_of_degrees / 2
edges = sum_of_degrees // 2
print("Number of edges =", edges)


# Step 5: Verify Handshaking Lemma
if sum_of_degrees == 2 * edges:
    print("\nHandshaking Lemma Verified ")
else:
    print("\nHandshaking Lemma Not Verified ")

