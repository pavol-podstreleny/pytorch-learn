import torch

x = torch.rand(5,3)
print(x)

# Indexing specific value
print(x[0,1])

# Range 
print(x[:,2])

# Specific Rows
print(x[(1,3),:])


