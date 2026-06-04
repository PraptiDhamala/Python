from math import comb

n = 1000  # total bits
r = 10    # error bits

possibilities = comb(n, r)

print("Number of possibilities =", possibilities)