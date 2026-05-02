vertices = ['P', 'Q', 'R', 'S']

edges = [("P","Q"),("P","S"),("Q","R"),("R","S")]

print(" ", end=" ")
for a in vertices:
    print(a, end=" ")
print();

for V in vertices:
    print(V, end=" ")
    for U in vertices:
        if (V,U) in edges:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print();
