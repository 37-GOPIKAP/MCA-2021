# construct the pattern using nested loop

for i in range(1, 10):
    j = 1
    if i > 5:
        limit = i - ((i % 5) + (i % 5))
    else:
        limit = i
    while (j <= limit):
        print(end="*")
        j += 1
    print(end="\n")
