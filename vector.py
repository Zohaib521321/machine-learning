import numpy as np
u=np.array([1,2,3])
v=np.array([3,5,6])
add=u+v
scalarMulti=2*v
dot=np.dot(u,v)
magnitud=np.linalg.norm(v)
unit=v/magnitud

print("u+v",add)
print("Scalar multiplication",scalarMulti)
print("dot product ",dot)
print("unit ",unit)