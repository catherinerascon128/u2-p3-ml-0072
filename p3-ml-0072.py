import numpy as np
n0072=np.array([10,20,30,40,50])
print(n0072)
print(n0072[0])
print(n0072[3])
print(n0072[-1])
print(n0072[-2])
print("--------------------------")
n0072=np.array([
    [10,20,30],
    [40,50,60]
])
print(n0072)
print(n0072[0, 0])
print(n0072[1, 2])
print(n0072[-1, -1])
print(n0072[-2, -2])
print("--------------------------")
# 3D array 2x(2x3)
n0072=np.array([
    [
            [10,20,30],
            [40,50,60]
    ],
    [
            [70,80,90],
            [100,110,120]
    ]
])
print(n0072)
print(n0072[0,0,1])
print(n0072[1,1,2])
print("catherine eileen huerta rascon NC = 0072")