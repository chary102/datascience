#euclidean_norm
def euclidean_norm(A,B):
    return sum((A[i]-B[i])**2 for i in range(len(A)))**0.5

A=[1,5,-2]
B=[4,11,7]
C=[7,-0,2]
print(euclidean_norm(A,B))
print(euclidean_norm(B,C))
print(euclidean_norm(C,A))



#manhattan_norm
def manhattan_norm(v):
    return sum(abs(x) for x in v)
A=[-1,0.5,3]
B=[4,8,25]
C=[77,-0.5,6]
print(manhattan_norm(A))
print(manhattan_norm(B))
print(manhattan_norm(C))



# max_norm
def max_norm(v):
    return max(abs(x) for x in v)
A=[-1,0.5,3]
B=[4,8,25]
C=[77,-0.5,6]
print(max_norm(A))
print(max_norm(B))
print(max_norm(C))

