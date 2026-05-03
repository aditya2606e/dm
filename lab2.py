print("p\t   q\t ¬(p∧q)\t  ¬p∨¬q")
print("- - - - - - - - - - - - - - - - - - - ")

equivalent = True

for p in [True, False]:
    for q in [True, False]:
        left = not (p and q)
        right = (not p) or (not q)

        print(p, "\t", q,  "\t", left, "\t", right)

        if left != right:
            equivalent = False

if equivalent:
    print("\nResult: Both propositions are logically equivalent.")
else:
    print("\nResult: Propositions are NOT logically equivalent.")
