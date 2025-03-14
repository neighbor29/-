pi0, pi1, V, s = [float(x) for x in input().split()]
s = s / 1000
RT = 8.31 * 293
k = 0.018 * 2340 * V / RT
result = (pi1 - pi0) * k / 100
t = 0
count = 0
while t < result:
    t += s
    count += 1
print(count)