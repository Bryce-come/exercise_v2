import math
from sympy import *

x = Symbol('x')
print(solve([x - (1 - 0.88 ** 24)]), [x])

import math
from sympy import *

x = Symbol('x')
print(solve([0.5 - (1 - 0.88 ** x)]), [x])
