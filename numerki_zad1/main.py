import numpy as np
import bisections
import front

f = lambda x: np.sin(x)

print(bisections.bisection_tolerance(f, 0.1, 3.2, 0.001))

# print(g(2.0))
# print(horner.horner_result([-2, 3, 2, -7.5], 2.0))

# front.choose_fuction_type()
front.choose_fuction_type()