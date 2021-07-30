n = int(input())
ans = []

for i in range(n):
    r = int(input())
    ans += [r]

print(min(ans))
print(max(ans))