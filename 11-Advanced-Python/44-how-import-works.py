# How import works in Python#

import math
print(math.floor(45.4545))

from math import sqrt, pi
print(sqrt(25))
print(pi)

from math import *
print(sqrt(49))
print(pi)

from math import sqrt as s
print(s(36))

import math
print(dir(math))

print(math.nan, type(math.nan))