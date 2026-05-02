# Defiine the sets
A = {1,2,3,4}
B = {3,4,5}

cartesian_product = []

for a in A:
    for b in B:
        cartesian_product.append((a, b))

# Display ordered pairs
print("A x B (Cartesian product):")
for pair in cartesian_product:
    print(pair)

# Display cardinality
print("Cardinality of A x B:", len(cartesian_product))
