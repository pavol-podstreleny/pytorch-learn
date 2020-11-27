# Tensors are similar to numpy's ndarrays + can run on GPU
import torch

# Create empty 5x3 matrix -> values are random values from memory
x = torch.empty(5,3)
print(x)

# Create randomly initialized 5x3 matrix
x = torch.rand(5,3)
print(x)

# Create 5x3 matrix with values from normal distribution
x = torch.randn(5,3)
print(x)

# Create 5x3 matrix with 0 values -> set dtype to long explicitely
x = torch.zeros(5,3,dtype=torch.long)
print(x)

# Create Tensor from python list
x = torch.tensor([5.5,3])
print(x)

# Create Tensor with same shape as x but random
x = torch.randn_like(x,dtype=torch.float)
print(x)

# Show size of the tensor
y = torch.randn(5,5)
# torch.Size support all tuple operations
print(y.size())

# One-element tensor -> use .item() to get Python number
x = torch.randn(1)
print(x)
print(x.item())
