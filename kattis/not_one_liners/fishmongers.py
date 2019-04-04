n, m = map(int, input().split())

fish = sorted(map(int, input().split()))
mong = sorted([tuple(map(int, input().split())) for _ in range(m)], key=(lambda m: m[1]), reverse=True)

total = 0
for (x, p) in mong:
	if len(fish) > 0:
		for i in range(x):
			if len(fish) > 0:
				total += fish.pop() * p
			else:
				break

print(total)
