import torch
import numpy as np
# The tensor and numpy will share their underlyin memory locations
# if the tensor is on CPU and changing one will change the other

# Converting tensor to numpy array
a = torch.ones(5)
print(a)

# Convert tensor to numpy
b = a.numpy()
print(b)

a.add_(1)
print(a)
print(b)

# All the tensors on the cpu except a CharTensor support converting to numpy and back
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a,1,out=a)
print(a)
print(b)

# Tensor can be moved onto any device using .to method | specifying device arg
if torch.cuda.is_available():
    device = torch.device("cuda")
    y = torch.ones_like(x,device=device) # We can specify device when creating
    x = x.to(device) # Or just move it to with to method
    z = x + y
    print(z)
    print(z.to("cpu",torch.double))
