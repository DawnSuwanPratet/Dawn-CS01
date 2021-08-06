Score = float(input())
Scores = []

while Score != -1:
    Scores += [Score]
    Score = float(input())

print()

Scores.sort()

for Score in Scores:
    print(Score)