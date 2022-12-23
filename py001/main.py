from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

import sys

#   idx goes up to 9, since .path's `__str__` is 10
sys.path.append('..∖∖modules')
for idx, p in enumerate(sys.path):
    print(f'Python will import from: {p}')