import torch

y = torch.ones(5,3)
x = torch.randn(5,3)

# Element-wise arithmetic operations
print(y + x)
print(y - x)
print(y / x)
print(y // x)
print(y ** x)

# We can write same operations in object-oriented way
print(torch.add(x,y))

# We can also provide third output argument to above method 
result = torch.empty(5,3)
torch.add(x,y,out=result)
print(result)

# We can perform also inplace addition
# Any operation that mutates a tensor in-place is post-fixed with an _
# For example x.copy_(y), x.t_() will change x
y.add_(x)
print(y)


