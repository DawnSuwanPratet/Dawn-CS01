[A, B, C] = input("Enter 3 types of animals: ").split()
A = str(A)
B = str(B)
C = str(C)
Animals = [A, B, C]

for s in Animals:
    if s == "Cat":
        print(s)