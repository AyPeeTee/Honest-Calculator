a = []
s = 0
while True:
    n = input()
    if n != ".":
        a.append(int(n))
    else:
        break
for n in a:
    s = n + s

print(s / len(a))
