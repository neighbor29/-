T = float(input())
p = float(input())
R = float(input())
tau = float(input())
if tau > T * 7 / 4:
    print('no', round((2 * tau - T * 7) * 24 * p * 3e8 * 3.6e3 / (100 * 2 * 1e12),
2))
else:
    print('yes', round(p * 3e6 / ((T * 7 - 2 * tau) * 3.6e3 * 24), 2))