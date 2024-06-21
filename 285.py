i = 0
while True:
    print(i)
    i += 1
    if i > 11:
        break

for j in range(10):
    if j < 0:
        continue
    print(j)