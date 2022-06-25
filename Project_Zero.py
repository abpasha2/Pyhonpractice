import numpy as np

#=========== Problem 5 =================#

def scalar_function(x, y):

    if x<=y:
        return x*y
    else:
        return x/y
    raise NotImplementedError

print(scalar_function(3,5))

def vector_function(x, y):

    return(np.vectorize(scalar_function)(x)(y))
    raise NotImplementedError

print(vector_function(scalar_function(3,5)))

# ===== Problem 4 ================######
# def neural_network(inputs, weights):
#    weights_trans = np.transpose(weights)
#    return np.tanh(np.matmul(inputs, weights_trans))
#    #Your code here
#    raise NotImplementedError

# a = np.array([[2],[3]])
# b = np.array([[2],[3]])

# print(neural_network(a,b))

# ===== Problem 3 ================######
# def norm(A, B):
#    return(np.linalg.norm(A+B))
#    raise NotImplementedError

# var_a = np.array([2, 3, 4]).T
# var_b = np.array([4, 5, 6]).T
# print(norm(var_a,var_b))


# ===== Problem 2 ================######
# def operations(h,w):
#    A = np.array(np.random.random([h,w]))
#    B = np.array(np.random.random([h,w]))
#    s = A+B
#    return A, B, s
#print(operations(2, 3))

# ===== Problem 1 ================######
# def randomization(n):
#    return (np.random.random([n, 1]))
#    raise NotImplementedError

# a = randomization(5)
# print(a)
